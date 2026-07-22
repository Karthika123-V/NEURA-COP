from dotenv import load_dotenv
from mem0 import MemoryClient
import logging
import json


load_dotenv()
user_name = 'Vikas'
mem0 = MemoryClient()

def add_memory():
    messages_formatted = [
    {
        "role": "user",
        "content": "My favorite food is biryani."
    },
    {
        "role": "assistant",
        "content": "Nice! Biryani is always a solid favorite."
    },
    {
        "role": "user",
        "content": "My favorite song is Nee Singam Dhan."
    },
    {
        "role": "assistant",
        "content": "That’s a powerful choice. Great song."
    },
    {
        "role": "user",
        "content": "I am an AI engineer."
    },
    {
        "role": "assistant",
        "content": "Awesome! AI engineering is a strong and exciting field."
    },
    {
        "role": "user",
        "content": "My hometown is Pudukkottai."
    },
    {
        "role": "assistant",
        "content": "Nice! Pudukkottai has a strong cultural vibe."
    },
    {
            "role": "user",
            "content": "My personal security code is 2707."
    },
    {
            "role": "assistant",
            "content": "Understood. I will remember your security code for verification."
    }
]

    mem0.add(messages_formatted, user_id="Vikas")

def get_memory_by_query():
    mem0 = MemoryClient()
    query = "What are {user_name}'s preferences?"
    results = mem0.search(query, user_id=user_name)

    memories = [
            {
                "memory": result["memory"],
                "updated_at": result["updated_at"]
            }
            for result in results
        ]
    memories_str = json.dumps(memories)
    print(f"Memories: {memories_str}")
    return memories_str


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    #get_memory_by_query()
    add_memory()
  
