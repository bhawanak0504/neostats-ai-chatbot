from langchain.embeddings import HuggingFaceEmbeddings
from config.config import EMBEDDING_MODEL


def load_embedding_model():
    try:
        embeddings = HuggingFaceEmbeddings(
            model_name=EMBEDDING_MODEL
        )
        return embeddings
    except Exception as e:
        raise RuntimeError(f"Embedding error: {str(e)}")