import json
from Code.client.client import client
from Code.assets.query2response import mongo_query
from Code.assets.promptNmessgaes import get_messages
from Code.assets.getTools import getTools

available_functions = {
    "mongo_query": mongo_query,
    }

tools = getTools()


async def response_from_bot(query:str) -> str:
    """
        Processes user input and returns natural response as bot's reply.

    Args:
        query (str): The input string containing user's natural language question.

    Returns:
        str : A natural response adhering to user's requirements
    """
    messages = get_messages(query,tools)
    # Make the initial request
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile", messages=messages, tools=tools, tool_choice="auto", max_completion_tokens=4096, temperature=0.5
    )

    response_message = response.choices[0].message
    tool_calls = response_message.tool_calls

    # Process tool calls
    messages.append(response_message)
    if tool_calls:
        for tool_call in tool_calls:
            function_name = tool_call.function.name
            function_to_call = available_functions[function_name]
            function_args = json.loads(tool_call.function.arguments)
            function_response = await function_to_call(**function_args)

            messages.append(
                {
                    "role": "tool",
                    "content": str(function_response),
                    "tool_call_id": tool_call.id,
                }
            )

        # Make the final request with tool call results
        final_response = client.chat.completions.create(
            model="llama-3.3-70b-versatile", messages=messages, tools=tools, tool_choice="auto", max_completion_tokens=4096
        )
        return (final_response.choices[0].message.content)
    else:
        return response_message.content

if __name__ == "__main__":
    query = "Find me 2 bedroom room in kathmandu"
    print ( response_from_bot(query) )