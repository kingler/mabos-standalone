import os
from openai import AsyncOpenAI

def create_openai_client():
    """
    Create and return an AsyncOpenAI client instance.

    This function initializes an AsyncOpenAI client using the API key
    stored in the OPENAI_API_KEY environment variable. If the API key
    is not set, it raises a ValueError.

    Returns:
        AsyncOpenAI: An instance of the AsyncOpenAI client.

    Raises:
        ValueError: If the OPENAI_API_KEY environment variable is not set.
    """
    if api_key := os.getenv("OPENAI_API_KEY"):
        return AsyncOpenAI(api_key=api_key)
    else:
        raise ValueError("OPENAI_API_KEY environment variable is not set")
openai_client = create_openai_client()
