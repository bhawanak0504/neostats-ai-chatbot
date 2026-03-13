import os
from dotenv import load_dotenv

load_dotenv()

# API KEYS
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Settings
DEFAULT_MODEL = "llama-3.1-8b-instant"
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"