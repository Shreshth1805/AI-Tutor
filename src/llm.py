from langchain_huggingface import HuggingFaceEndpoint
from src.config import api_key

def llm():
    llm=HuggingFaceEndpoint(
        repo_id="mistralai/Mistral-7B-Instruct-v0.2",
        huggingfacehub_api_tokrn=api_key,
        temperature=.5,
        max_new_tokens=512
    )
    return llm