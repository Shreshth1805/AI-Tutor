from langchain_huggingface import HuggingFaceEndpoint
from src.config import api_key

def get_llm():
    llm=HuggingFaceEndpoint(
        repo_id="google/flan-t5-large",
        huggingfacehub_api_token=api_key,
        temperature=.5,
        max_new_tokens=512
    )
    return llm