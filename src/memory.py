from langchain.memory import ConversationalBufferMemory

memory=ConversationalBufferMemory(
    memory_key="chat_history",
    return_messages=True
)
