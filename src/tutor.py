from langchain.chains import ConversationalRetrievalChain
from src.llm import get_llm
from src.memory import memory
def tutor_chain(retriever):
    llm=get_llm()
    chain=ConversationalRetrievalChain(
        llm=llm,
        retriever=retriever,
        memory=memory,
        return_source_documents=True
    )
    return chain