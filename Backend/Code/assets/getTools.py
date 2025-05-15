from typing import List, Dict

def getTools() -> list[Dict]:    
    tools = [
        {
        "type": "function",
        "function": {
            "name": "mongo_query",
            "description": "Executes a MongoDB query based on user natural language question and returns a list of matching documents.",
            "parameters": {
                "type": "object",
                "properties": {
                    "user_input": {
                        "type": "string",
                        "description": "Natural language input specifying what data to retrieve from the MongoDB database."
                    }
                },
                "required": ["user_input"],
            },
        },
        }
    ]
    return tools