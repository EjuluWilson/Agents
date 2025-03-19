from langchain_core.messages import HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from langchain_core.tools import StructuredTool
from langgraph.graph import StateGraph, END
from typing import TypedDict, List, Union, Dict, Literal
import snake
import os
from pydantic import BaseModel, Field

# 1. Define the state
class AgentState(TypedDict):
    messages: List[Union[HumanMessage, AIMessage]]
    current_position: Dict[str, int]
    goal_position: Dict[str, int]
    grid_size: int
    game_status: Literal["on", "done"]
    tool_calls: List[Dict]

# 2. Define the tool schemas with coordinate parameters
class MoveToInput(BaseModel):
    x: int = Field(..., description="The x-coordinate to move to")
    y: int = Field(..., description="The y-coordinate to move to")

# Define the moveTo tool as a schema object for the LLM
move_to_tool = StructuredTool.from_function(
    name="move_to",
    description="Move the player to the specified coordinates (x, y)",
    func=lambda x, y: f"Move to position ({x}, {y})",
    args_schema=MoveToInput
)

# List of tools to expose to the LLM
tools = [move_to_tool]

# 3. Initialize LLM with tool calling capability
llm = ChatOpenAI(
    model="gpt-4-turbo",
    temperature=0,
    api_key=os.environ.get("OPENAI_API_KEY")
)

# The actual game instance will be created in the execution node
game_instance = None

# Function to create the game state
def initialize_game_node(state: AgentState) -> AgentState:
    """Initialize the game and update the state."""
    global game_instance
    
    # Create a new game instance
    game_instance = snake.GridGame()
    game_info = game_instance.startGame()
    
    # Update the state with the game info
    state["current_position"] = game_info["current_position"]
    state["goal_position"] = game_info["goal_position"]
    state["grid_size"] = game_info["grid_size"]
    state["game_status"] = "on"
    
    # Add a message about the game state to the messages
    initial_message = f"Game initialized. Player at position ({state['current_position']['x']}, {state['current_position']['y']}). Goal at ({state['goal_position']['x']}, {state['goal_position']['y']})."
    state["messages"].append(AIMessage(content=initial_message))
    
    return state

# Function to decide on the next move
def decide_move_node(state: AgentState) -> AgentState:
    """Use the LLM to decide on the next move by specifying coordinates."""
    # Get the position information from the state
    current_pos = state["current_position"]
    goal_pos = state["goal_position"]
    grid_size = state["grid_size"]
    
    # Prepare context for the LLM
    context = f"Current position: ({current_pos['x']}, {current_pos['y']}). Goal position: ({goal_pos['x']}, {goal_pos['y']}). Grid size: {grid_size}x{grid_size}."
    
    # Create a prompt for the LLM
    prompt = f"""
    You are playing a grid-based game. {context}
    
    Your goal is to reach the target position.
    You can only move to adjacent cells (one step at a time, horizontally or vertically).
    
    Available tool:
    - move_to(x: int, y: int): Move the player to the specified coordinates
    
    Choose the best move to get closer to the goal. Remember:
    1. You can only move one step at a time to an adjacent cell
    2. Valid moves are to cells that share an edge with your current position
    3. You cannot move diagonally
    4. You cannot move outside the grid boundaries (0 to {grid_size - 1})
    
    Determine the coordinates you want to move to and call the move_to tool.
    IMPORTANT: Only generate tool calls. Don't try to execute them directly.
    """
    
    # Add the prompt to the messages
    state["messages"].append(HumanMessage(content=prompt))
    
    # Get the LLM's response
    response = llm.bind_tools(tools).invoke(state["messages"])
    
    # Add the response to the messages
    state["messages"].append(response)
    
    # Extract the tool calls from the response
    state["tool_calls"] = response.tool_calls if hasattr(response, "tool_calls") else []
    
    return state

# Function to execute the tool calls
def execute_tools_node(state: AgentState) -> AgentState:
    """Execute the tool calls made by the LLM."""
    global game_instance
    
    # Get the tool calls
    tool_calls = state["tool_calls"]
    
    # Execute each tool call
    for tool_call in tool_calls:
        # Get the tool name and arguments
        tool_name = tool_call["name"]
        tool_args = tool_call.get("args", {})
        
        if tool_name == "move_to" and "x" in tool_args and "y" in tool_args:
            x = tool_args["x"]
            y = tool_args["y"]
            
            # Execute the moveTo command
            result = game_instance.moveTo(x, y)
            
            # Update the state with the new position
            state["current_position"] = result["current_position"]
            
            # Check if the move was successful
            if result["success"]:
                message = f"{result['message']}"
                
                # Check if the game is won
                if result["win"]:
                    message += " You reached the goal!"
                    state["game_status"] = "done"
            else:
                message = f"Invalid move: {result['message']}"
                
            # Add the result to the messages
            state["messages"].append(AIMessage(content=message))
        else:
            error_message = f"Invalid tool call: {tool_name} or missing coordinates"
            state["messages"].append(AIMessage(content=error_message))
    
    # Clear the tool calls for the next iteration
    state["tool_calls"] = []
    
    return state

# Function to decide whether to continue or end
def should_continue(state: AgentState) -> Union[Literal["decide_move"], Literal["END"]]:
    """Decide whether to continue the game or end it."""
    if state["game_status"] == "done":
        return END
    else:
        return "decide_move"

# Build the graph
def build_agent():
    # Create a new graph
    workflow = StateGraph(AgentState)
    
    # Add the nodes
    workflow.add_node("initialize_game", initialize_game_node)
    workflow.add_node("decide_move", decide_move_node)
    workflow.add_node("execute_tools", execute_tools_node)
    
    # Add the edges
    workflow.add_edge("initialize_game", "decide_move")
    workflow.add_edge("decide_move", "execute_tools")
    workflow.add_conditional_edges(
        "execute_tools",
        should_continue
    )
    
    # Set the entry point
    workflow.set_entry_point("initialize_game")
    
    # Compile the graph
    return workflow.compile()

# Run the agent
def run_agent():
    # Build the agent
    agent = build_agent()
    
    # Initialize the state
    initial_state = {
        "messages": [],
        "current_position": {"x": 0, "y": 0},  # These will be overwritten in initialize_game_node
        "goal_position": {"x": 0, "y": 0},     # These will be overwritten in initialize_game_node
        "grid_size": 3,                        # This will be overwritten in initialize_game_node
        "game_status": "on",
        "tool_calls": []
    }
    
    # Run the agent
    for state in agent.stream(initial_state):
        # Print the latest message
        if state.get("messages") and len(state["messages"]) > 0:
            latest_message = state["messages"][-1]
            print(f"{latest_message.type}: {latest_message.content}")
            
            # If there are tool calls, print them
            if hasattr(latest_message, "tool_calls") and latest_message.tool_calls:
                for tool_call in latest_message.tool_calls:
                    print(f"Tool call: {tool_call['name']}({tool_call['args']})")

if __name__ == "__main__":
    run_agent()