import os
from langchain.vectorstores import FAISS
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from models.embeddings import load_embedding_model


def create_vector_store(file_path):

    loader = PyPDFLoader(file_path)
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    texts = splitter.split_documents(docs)

    embeddings = load_embedding_model()

    vector_store = FAISS.from_documents(texts, embeddings)

    return vector_store


def search_docs(vector_store, query):

    docs = vector_store.similarity_search(query, k=3)

    return "\n".join([doc.page_content for doc in docs])