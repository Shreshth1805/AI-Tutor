from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vecorstores import FAISS
from src.embeddings import huggingface_embeddings
def vector_db(text):
    text_splitter=RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=50)
    docs=text_splitter.create_documents([text])
    embeddings=huggingface_embeddings()
    db=FAISS.from_documents(docs,embeddings)
    return db

def retriever(vector_db):
    return vector_db.as_retriever(
        search_kwargs={"k":4}
    )