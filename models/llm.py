from langchain_groq import ChatGroq
from config.config import GROQ_API_KEY


def get_chatgroq_model():

    model = ChatGroq(
        api_key=GROQ_API_KEY,
        model="llama-3.1-8b-instant",
        temperature=0.7
    )

    return model