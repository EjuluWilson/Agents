from langchain_core.messages import HumanMessage, AIMessage, ToolMessage
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langgraph.graph import StateGraph, END  # Add END here
from typing import TypedDict, List, Union, Dict, Literal
import snake
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv(dotenv_path="../.env")

# Define the state
class AgentState(TypedDict):
    messages: List[Union[HumanMessage, AIMessage, ToolMessage]]
    current_position: Dict[str, int]
    goal_position: Dict[str, int]
    grid_size: int
    game_status: Literal["on", "done"]
    is_initialized: bool

# Define the tool
@tool
def move(direction: str) -> str:
    """Move the player in the specified direction: U (up), D (down), L (left), or R (right)"""
    return f"Move in direction {direction}"

# Create the agent graph
def create_agent_graph():
    # Initialize the graph
    workflow = StateGraph(AgentState)
    
    # Add nodes
    workflow.add_node("initialize_game", initialize_game_node)
    workflow.add_node("process_move", process_move_node)
    
    # Add conditional edges based on initialization status
    workflow.add_conditional_edges(
        "initialize_game",
        lambda state: "process_move" if state["is_initialized"] else "initialize_game"
    )
    
    # Make process_move always go to END
    workflow.add_edge("process_move", END)
    
    # Set the entry point
    workflow.set_entry_point("initialize_game")
    
    # Compile the graph
    return workflow.compile()

# Global game instance
game_instance = None

# Initialize game node
def initialize_game_node(state: AgentState) -> AgentState:
    global game_instance
    
    # Only initialize if not already initialized
    if not state["is_initialized"]:
        game_instance = snake.GridGame()
        game_info = game_instance.startGame()
        
        state["current_position"] = game_info["current_position"]
        state["goal_position"] = game_info["goal_position"]
        state["grid_size"] = game_info["grid_size"]
        state["is_initialized"] = True
        
        state["messages"].append(AIMessage(content=f"Game initialized. Player at ({state['current_position']['x']}, {state['current_position']['y']}). Goal at ({state['goal_position']['x']}, {state['goal_position']['y']})."))
    
    return state

# Process move node (combines LLM decision and execution)
def process_move_node(state: AgentState) -> AgentState:
    global game_instance
    
    # Skip if game is done
    if state["game_status"] == "done":
        return state
    
    # Get LLM to decide the move
    llm = ChatOpenAI(
        model="gpt-4-turbo",
        temperature=0,
        api_key=os.environ.get("OPENAI_API_KEY")
    )
    
    # Prepare context for the LLM
    context = f"Current position: ({state['current_position']['x']}, {state['current_position']['y']}). Goal position: ({state['goal_position']['x']}, {state['goal_position']['y']}). Grid size: {state['grid_size']}x{state['grid_size']}."
    
    # Create a prompt for the LLM
    
    # Update this part in the process_move_node function
    prompt = f"""
    You are playing a grid-based game. {context}

    Your goal is to reach the target position.
    You can move one step at a time in four directions:
    - U (up): Decreases the y-coordinate by 1
    - D (down): Increases the y-coordinate by 1
    - L (left): Decreases the x-coordinate by 1
    - R (right): Increases the x-coordinate by 1

    Coordinate system: (0,0) is at the top-left, x increases moving right, y increases moving down.

    Available tool:
    - move(direction: str): Move the player in the specified direction (U, D, L, R)

    Analyze the current position and goal position carefully.
    Choose the best move to get closer to the goal by comparing x and y coordinates separately.
    Consider BOTH horizontal AND vertical movement to find the shortest path.
    """
   
    # Add the prompt to the messages
    state["messages"].append(HumanMessage(content=prompt))
    
    # Get the LLM's response
    response = llm.bind_tools([move]).invoke(state["messages"])
    
    # Add the response to the messages
    state["messages"].append(response)
    
    # Extract the direction from the tool call
    if hasattr(response, "tool_calls") and response.tool_calls:
        for tool_call in response.tool_calls:
            tool_call_id = tool_call["id"]
            tool_name = tool_call["name"]
            
            if tool_name == "move" and "direction" in tool_call["args"]:
                direction = tool_call["args"]["direction"]
                
                # Execute the move
                result = game_instance.move(direction)
                
                # Update the state
                state["current_position"] = result["current_position"]
                
                # Create a ToolMessage with the appropriate status
                status = "success" if result["success"] else "error"
                
                # Add the tool message to the state
                tool_message = ToolMessage(
                    content=result["message"],
                    tool_call_id=tool_call_id,
                    name=tool_name,
                    status=status
                )
                state["messages"].append(tool_message)
                
                # Check if game is won
                if result["win"]:
                    state["messages"].append(AIMessage(content="You reached the goal!"))
                    state["game_status"] = "done"
            else:
                # Handle invalid tool call
                error_message = f"Invalid tool call or missing direction"
                tool_message = ToolMessage(
                    content=error_message,
                    tool_call_id=tool_call_id,
                    name=tool_name,
                    status="error"
                )
                state["messages"].append(tool_message)
    
    return state

# Function to handle each event
def handle_game_event(state=None):
    """Run one complete step of the game."""
    # Create the agent graph
    agent = create_agent_graph()
    
    # Initialize state if needed
    if state is None:
        state = {
            "messages": [],
            "current_position": {"x": 0, "y": 0},
            "goal_position": {"x": 0, "y": 0},
            "grid_size": 3,
            "game_status": "on",
            "is_initialized": False
        }
    
    # Run the graph once
    result = agent.invoke(state)
    
    # Print the latest messages for this step
    if len(result["messages"]) > len(state["messages"]):
        for i in range(len(state["messages"]), len(result["messages"])):
            msg = result["messages"][i]
            print(f"{msg.type}: {msg.content}")
            
            # If there are tool calls, print them
            if hasattr(msg, "tool_calls") and msg.tool_calls:
                for tool_call in msg.tool_calls:
                    args_str = ', '.join([f"{k}={v}" for k, v in tool_call['args'].items()])
                    print(f"Tool call: {tool_call['name']}({args_str})")
    
    # Return the updated state
    return result

# Interactive simulation
def run_interactive():
    """Run the agent interactively via terminal commands."""
    state = None
    print("Interactive Snake Game Agent")
    print("Type 'n' to make a move, or 'exit' to quit")
    
    while True:
        command = input("🐍 ").strip().lower()
        
        if command == "exit()":
            break
        elif command == "n":
            state = handle_game_event(state)
            # Check if game is over
            if state["game_status"] == "done":
                print("Game complete! Type 'next' to start a new game or 'exit' to quit")
                # Reset state to start new game
                state = None
        else:
            print("Unknown command")

if __name__ == "__main__":
    run_interactive()