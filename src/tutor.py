from langchain.chains import ConversationalRetrievalChain
from src.llm import llm
from src.memory import memory
def tutor_chain(retriever):
    llm=llm()
    chain=ConversationalRetrievalChain(
        llm=llm,
        retriever=retriever,
        memory=memory,
        return_source_documents=True
    )
    return chain