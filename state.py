from langchain_core.messages import HumanMessage, AIMessage, ToolMessage

{
    "messages": [
        AIMessage(
            content="Game initialized. Player at (0, 2). Goal at (1, 0).",
            additional_kwargs={},
            response_metadata={},
        )
    ],
    "current_position": {"x": 0, "y": 2},
    "goal_position": {"x": 1, "y": 0},
    "grid_size": 3,
    "game_status": "on",
    "is_initialized": True,
}
{
    "messages": [
        AIMessage(
            content="Game initialized. Player at (0, 2). Goal at (1, 0).",
            additional_kwargs={},
            response_metadata={},
        ),
        HumanMessage(
            content="\n    You are playing a grid-based game. Current position: (0, 2). Goal position: (1, 0). Grid size: 3x3.\n    \n    Your goal is to reach the target position.\n    You can move one step at a time in four directions.\n    \n    Available tool:\n    - move(direction: str): Move the player in the specified direction (U, D, L, R)\n      where: U = up, D = down, L = left, R = right\n    \n    Choose the best move to get closer to the goal.\n    ",
            additional_kwargs={},
            response_metadata={},
        ),
        AIMessage(
            content="",
            additional_kwargs={
                "tool_calls": [
                    {
                        "id": "call_bveNaMJ0DWvicgHiAxAa4dl5",
                        "function": {"arguments": '{"direction": "D"}', "name": "move"},
                        "type": "function",
                    },
                    {
                        "id": "call_GUclhFvGxcdSEaRNYEPsVW1l",
                        "function": {"arguments": '{"direction": "L"}', "name": "move"},
                        "type": "function",
                    },
                ],
                "refusal": None,
            },
            response_metadata={
                "token_usage": {
                    "completion_tokens": 42,
                    "prompt_tokens": 205,
                    "total_tokens": 247,
                    "completion_tokens_details": {
                        "accepted_prediction_tokens": 0,
                        "audio_tokens": 0,
                        "reasoning_tokens": 0,
                        "rejected_prediction_tokens": 0,
                    },
                    "prompt_tokens_details": {"audio_tokens": 0, "cached_tokens": 0},
                },
                "model_name": "gpt-4-turbo-2024-04-09",
                "system_fingerprint": "fp_bf9cb2c77f",
                "finish_reason": "tool_calls",
                "logprobs": None,
            },
            id="run-57022609-b613-4237-a76d-3a3ca24b4e6f-0",
            tool_calls=[
                {
                    "name": "move",
                    "args": {"direction": "D"},
                    "id": "call_bveNaMJ0DWvicgHiAxAa4dl5",
                    "type": "tool_call",
                },
                {
                    "name": "move",
                    "args": {"direction": "L"},
                    "id": "call_GUclhFvGxcdSEaRNYEPsVW1l",
                    "type": "tool_call",
                },
            ],
            usage_metadata={
                "input_tokens": 205,
                "output_tokens": 42,
                "total_tokens": 247,
                "input_token_details": {"audio": 0, "cache_read": 0},
                "output_token_details": {"audio": 0, "reasoning": 0},
            },
        ),
        AIMessage(
            content="Invalid move: out of bounds",
            additional_kwargs={},
            response_metadata={},
        ),
    ],
    "current_position": {"x": 0, "y": 2},
    "goal_position": {"x": 1, "y": 0},
    "grid_size": 3,
    "game_status": "on",
    "is_initialized": True,
}
{
    "messages": [
        AIMessage(
            content="Game initialized. Player at (0, 2). Goal at (1, 0).",
            additional_kwargs={},
            response_metadata={},
        ),
        HumanMessage(
            content="\n    You are playing a grid-based game. Current position: (0, 2). Goal position: (1, 0). Grid size: 3x3.\n    \n    Your goal is to reach the target position.\n    You can move one step at a time in four directions.\n    \n    Available tool:\n    - move(direction: str): Move the player in the specified direction (U, D, L, R)\n      where: U = up, D = down, L = left, R = right\n    \n    Choose the best move to get closer to the goal.\n    ",
            additional_kwargs={},
            response_metadata={},
        ),
        AIMessage(
            content="",
            additional_kwargs={
                "tool_calls": [
                    {
                        "id": "call_bveNaMJ0DWvicgHiAxAa4dl5",
                        "function": {"arguments": '{"direction": "D"}', "name": "move"},
                        "type": "function",
                    },
                    {
                        "id": "call_GUclhFvGxcdSEaRNYEPsVW1l",
                        "function": {"arguments": '{"direction": "L"}', "name": "move"},
                        "type": "function",
                    },
                ],
                "refusal": None,
            },
            response_metadata={
                "token_usage": {
                    "completion_tokens": 42,
                    "prompt_tokens": 205,
                    "total_tokens": 247,
                    "completion_tokens_details": {
                        "accepted_prediction_tokens": 0,
                        "audio_tokens": 0,
                        "reasoning_tokens": 0,
                        "rejected_prediction_tokens": 0,
                    },
                    "prompt_tokens_details": {"audio_tokens": 0, "cached_tokens": 0},
                },
                "model_name": "gpt-4-turbo-2024-04-09",
                "system_fingerprint": "fp_bf9cb2c77f",
                "finish_reason": "tool_calls",
                "logprobs": None,
            },
            id="run-57022609-b613-4237-a76d-3a3ca24b4e6f-0",
            tool_calls=[
                {
                    "name": "move",
                    "args": {"direction": "D"},
                    "id": "call_bveNaMJ0DWvicgHiAxAa4dl5",
                    "type": "tool_call",
                },
                {
                    "name": "move",
                    "args": {"direction": "L"},
                    "id": "call_GUclhFvGxcdSEaRNYEPsVW1l",
                    "type": "tool_call",
                },
            ],
            usage_metadata={
                "input_tokens": 205,
                "output_tokens": 42,
                "total_tokens": 247,
                "input_token_details": {"audio": 0, "cache_read": 0},
                "output_token_details": {"audio": 0, "reasoning": 0},
            },
        ),
        AIMessage(
            content="Invalid move: out of bounds",
            additional_kwargs={},
            response_metadata={},
        ),
    ],
    "current_position": {"x": 0, "y": 0},
    "goal_position": {"x": 0, "y": 0},
    "grid_size": 3,
    "game_status": "on",
    "is_initialized": False,
}


{
    "messages": [
        HumanMessage(
            content="Calculate (10 + 5) * 2 - 4 / 2.",
            additional_kwargs={},
            response_metadata={},
            id="03fcfc6e-b8b7-4c4c-8034-4f02fada34d8",
        ),
        AIMessage(
            content="",
            additional_kwargs={
                "tool_calls": [
                    {
                        "id": "call_mXN4sAiY44YtjcobmxChTkCT",
                        "function": {"arguments": '{"a": 10, "b": 5}', "name": "add"},
                        "type": "function",
                    },
                    {
                        "id": "call_LMIbajTAAEe2AF7HtYeBzCLU",
                        "function": {
                            "arguments": '{"a": 15, "b": 2}',
                            "name": "multiply",
                        },
                        "type": "function",
                    },
                    {
                        "id": "call_yeyDJuGwokZ8foDi1RxMCWIZ",
                        "function": {"arguments": '{"a": 4, "b": 2}', "name": "divide"},
                        "type": "function",
                    },
                    {
                        "id": "call_qrc1ek0zGQhzKJm3wfALjkIz",
                        "function": {
                            "arguments": '{"a": 30, "b": 2}',
                            "name": "subtract",
                        },
                        "type": "function",
                    },
                ],
                "refusal": None,
            },
            response_metadata={
                "token_usage": {
                    "completion_tokens": 84,
                    "prompt_tokens": 191,
                    "total_tokens": 275,
                    "completion_tokens_details": {
                        "accepted_prediction_tokens": 0,
                        "audio_tokens": 0,
                        "reasoning_tokens": 0,
                        "rejected_prediction_tokens": 0,
                    },
                    "prompt_tokens_details": {"audio_tokens": 0, "cached_tokens": 0},
                },
                "model_name": "gpt-3.5-turbo-0125",
                "system_fingerprint": None,
                "finish_reason": "tool_calls",
                "logprobs": None,
            },
            id="run-ab547bda-aaea-4923-a448-f4b9bb0b577e-0",
            tool_calls=[
                {
                    "name": "add",
                    "args": {"a": 10, "b": 5},
                    "id": "call_mXN4sAiY44YtjcobmxChTkCT",
                    "type": "tool_call",
                },
                {
                    "name": "multiply",
                    "args": {"a": 15, "b": 2},
                    "id": "call_LMIbajTAAEe2AF7HtYeBzCLU",
                    "type": "tool_call",
                },
                {
                    "name": "divide",
                    "args": {"a": 4, "b": 2},
                    "id": "call_yeyDJuGwokZ8foDi1RxMCWIZ",
                    "type": "tool_call",
                },
                {
                    "name": "subtract",
                    "args": {"a": 30, "b": 2},
                    "id": "call_qrc1ek0zGQhzKJm3wfALjkIz",
                    "type": "tool_call",
                },
            ],
            usage_metadata={
                "input_tokens": 191,
                "output_tokens": 84,
                "total_tokens": 275,
                "input_token_details": {"audio": 0, "cache_read": 0},
                "output_token_details": {"audio": 0, "reasoning": 0},
            },
        ),
        ToolMessage(
            content="15.0",
            name="add",
            id="f63762b6-31f8-4847-ab73-0add040206d3",
            tool_call_id="call_mXN4sAiY44YtjcobmxChTkCT",
        ),
        ToolMessage(
            content="30.0",
            name="multiply",
            id="cfd2d698-920b-4a1d-812d-bbec10a75037",
            tool_call_id="call_LMIbajTAAEe2AF7HtYeBzCLU",
        ),
        ToolMessage(
            content="2.0",
            name="divide",
            id="ff62c19c-071a-4bf3-9383-d14b3f2a42f4",
            tool_call_id="call_yeyDJuGwokZ8foDi1RxMCWIZ",
        ),
        ToolMessage(
            content="28.0",
            name="subtract",
            id="76a8bfa9-6976-43b0-a779-b66534309231",
            tool_call_id="call_qrc1ek0zGQhzKJm3wfALjkIz",
        ),
        AIMessage(
            content="",
            additional_kwargs={
                "tool_calls": [
                    {
                        "id": "call_IMAhpBA3O8UAlbT9tQXYij9E",
                        "function": {"arguments": '{"a":30,"b":2}', "name": "subtract"},
                        "type": "function",
                    }
                ],
                "refusal": None,
            },
            response_metadata={
                "token_usage": {
                    "completion_tokens": 18,
                    "prompt_tokens": 304,
                    "total_tokens": 322,
                    "completion_tokens_details": {
                        "accepted_prediction_tokens": 0,
                        "audio_tokens": 0,
                        "reasoning_tokens": 0,
                        "rejected_prediction_tokens": 0,
                    },
                    "prompt_tokens_details": {"audio_tokens": 0, "cached_tokens": 0},
                },
                "model_name": "gpt-3.5-turbo-0125",
                "system_fingerprint": None,
                "finish_reason": "tool_calls",
                "logprobs": None,
            },
            id="run-c59c26cc-0974-471e-bfd9-7a935d807b3d-0",
            tool_calls=[
                {
                    "name": "subtract",
                    "args": {"a": 30, "b": 2},
                    "id": "call_IMAhpBA3O8UAlbT9tQXYij9E",
                    "type": "tool_call",
                }
            ],
            usage_metadata={
                "input_tokens": 304,
                "output_tokens": 18,
                "total_tokens": 322,
                "input_token_details": {"audio": 0, "cache_read": 0},
                "output_token_details": {"audio": 0, "reasoning": 0},
            },
        ),
        ToolMessage(
            content="28.0",
            name="subtract",
            id="f9c543d3-fb73-4e6b-bf7c-3416217ef32e",
            tool_call_id="call_IMAhpBA3O8UAlbT9tQXYij9E",
        ),
        AIMessage(
            content="28.0",
            additional_kwargs={"refusal": None},
            response_metadata={
                "token_usage": {
                    "completion_tokens": 5,
                    "prompt_tokens": 331,
                    "total_tokens": 336,
                    "completion_tokens_details": {
                        "accepted_prediction_tokens": 0,
                        "audio_tokens": 0,
                        "reasoning_tokens": 0,
                        "rejected_prediction_tokens": 0,
                    },
                    "prompt_tokens_details": {"audio_tokens": 0, "cached_tokens": 0},
                },
                "model_name": "gpt-3.5-turbo-0125",
                "system_fingerprint": None,
                "finish_reason": "stop",
                "logprobs": None,
            },
            id="run-4b14dd9b-cc3f-487a-88d9-6e54d9ae0d76-0",
            usage_metadata={
                "input_tokens": 331,
                "output_tokens": 5,
                "total_tokens": 336,
                "input_token_details": {"audio": 0, "cache_read": 0},
                "output_token_details": {"audio": 0, "reasoning": 0},
            },
        ),
    ]
}
