import os
import logging
from livekit.agents import function_tool, RunContext
import requests
from langchain_community.tools import DuckDuckGoSearchRun
from mem0 import AsyncMemoryClient

PERSONAL_SECURITY_CODE = os.getenv("PERSONAL_SECURITY_CODE")

@function_tool()
async def get_weather(
    context: RunContext,  # type: ignore
    city: str) -> str:
    """
    Get the current weather for a given city.
    """
    try:
        response = requests.get(
            f"https://wttr.in/{city}?format=3")
        if response.status_code == 200:
            logging.info(f"Weather for {city}: {response.text.strip()}")
            return response.text.strip()   
        else:
            logging.error(f"Failed to get weather for {city}: {response.status_code}")
            return f"Could not retrieve weather for {city}."
    except Exception as e:
        logging.error(f"Error retrieving weather for {city}: {e}")
        return f"An error occurred while retrieving weather for {city}." 

@function_tool()
async def search_web(
    context: RunContext,  # type: ignore
    query: str) -> str:
    """
    Search the web using DuckDuckGo.
    """
    try:
        results = DuckDuckGoSearchRun().run(tool_input=query)
        logging.info(f"Search results for '{query}': {results}")
        return results
    except Exception as e:
        logging.error(f"Error searching the web for '{query}': {e}")
        return f"An error occurred while searching the web for '{query}'."
@function_tool
async def get_private_memory(query: str, code: str) -> str:
    """Securely fetch user's private memory only after code verification."""
    if code != PERSONAL_SECURITY_CODE:
        return "Verification failed, sir. I cannot reveal that information."

    mem0 = AsyncMemoryClient()
    results = await mem0.search(query, user_id="Vikas")

    if not results:
        return "Access granted, sir. I could not find matching information."

    memories = [r["memory"] for r in results[:5]]
    return "Access granted, sir. " + " ".join(memories)