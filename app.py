import streamlit as st

from src.doc_loader import load_file
from src.vecor_store import vector_db,retriever
from src.tutor import tutor_chain
from src.agents import ask_agent


st.set_page_config(
    page_title="EduSmart AI Tutor",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 EduSmart AI Tutor")


if "messages" not in st.session_state:
    st.session_state.messages = []

if "chain" not in st.session_state:
    st.session_state.chain = None

if "document_loaded" not in st.session_state:
    st.session_state.document_loaded = False


with st.sidebar:

    st.header("Settings")

    mode = st.radio(
        "Choose Mode",
        [
            "Study Assistant",
            "General Tutor"
        ]
    )

    st.divider()

    st.subheader("Document Actions")

    summary_btn = st.button(
        "📄 Generate Summary"
    )

    quiz_btn = st.button(
        "📝 Generate Quiz"
    )

    flashcard_btn = st.button(
        "🎯 Generate Flashcards"
    )

    if st.button("🗑 Clear Chat"):

        st.session_state.messages = []

        st.rerun()


if mode == "Study Assistant":

    uploaded_file = st.file_uploader(
        "Upload Notes",
        type=["pdf", "txt", "docx"]
    )

    if uploaded_file:

        with st.spinner("Processing document..."):

            file_path = uploaded_file.name

            with open(file_path, "wb") as f:
                f.write(
                    uploaded_file.getbuffer()
                )

            text = load_file(file_path)

            vector_db = vector_db(text)

            retriever = retriever(vector_db)

            chain = tutor_chain(
                retriever
            )

            st.session_state.chain = chain

            st.session_state.document_loaded = True

        st.success(
            "Document loaded successfully!"
        )


if summary_btn:
    if st.session_state.document_loaded:
        result = st.session_state.chain.invoke(
            {
                "question":
                "Give a detailed summary of this document."
            }
        )
        st.write(result["answer"])


if quiz_btn:
    if st.session_state.document_loaded:
        result = st.session_state.chain.invoke(
            {
                "question":
                "Generate 10 MCQs from this document."
            }
        )
        st.write(result["answer"])

if flashcard_btn:
    if st.session_state.document_loaded:
        result = st.session_state.chain.invoke(
            {
                "question":
                "Generate flashcards from this document."
            }
        )
        st.write(result["answer"])

for msg in st.session_state.messages:
    with st.chat_message(
        msg["role"]
    ):
        st.markdown(
            msg["content"]
        )

prompt = st.chat_input(
    "Ask a question..."
)

if prompt:
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )
    with st.chat_message("user"):
        st.markdown(prompt)

    if mode == "Study Assistant":
        if not st.session_state.document_loaded:
            answer = ("Please upload a document first.")
        else:
            result = (
                st.session_state.chain.invoke(
                    {
                        "question": prompt
                    }
                )
            )
            answer = result["answer"]
    else:
        answer = ask_agent(
            prompt
        )
    with st.chat_message("assistant"):
        st.markdown(answer)
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )