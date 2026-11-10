import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

DEFAULT_MODEL = "openai/gpt-oss-120b"


def get_groq_model(model: str = DEFAULT_MODEL, temperature: float = 0.0) -> ChatGroq:
    """Return a ChatGroq chat model using GROQ_API_KEY from the environment/.env."""
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise RuntimeError("GROQ_API_KEY is not set. Add it to your .env file.")
    return ChatGroq(model=model, temperature=temperature, api_key=api_key)


if __name__ == "__main__":
    import sys

    sys.stdout.reconfigure(encoding="utf-8")  # Windows console defaults to cp1252
    model = get_groq_model()
    response = model.invoke("which model are you")
    print(response.content)