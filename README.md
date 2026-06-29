# 🎓 EduSmart AI Tutor

An AI-powered educational assistant built using LangChain, Hugging Face Embeddings, Groq LLMs, FAISS, and Streamlit.

EduSmart AI Tutor helps students learn more effectively through document-based question answering, AI tutoring, research assistance, summarization, quiz generation, and personalized learning experiences.

---

# 🚀 Features

## 📚 Document-Based Learning (RAG)

Students can upload:

* PDF files
* DOCX files
* TXT files

The system:

1. Extracts content from uploaded documents
2. Splits text into chunks
3. Creates embeddings using MiniLM
4. Stores vectors in FAISS
5. Retrieves relevant information
6. Generates contextual answers using an LLM

---

## 🤖 General AI Tutor

Students can ask general questions such as:

* Explain Machine Learning
* What is Photosynthesis?
* How does Blockchain work?
* Explain Newton’s Laws

The tutor provides conversational and educational responses.

---

## 🌐 Wikipedia Tool

The tutor can retrieve information from Wikipedia for factual and historical topics.

Examples:

* Who was Albert Einstein?
* History of the Internet
* What is Quantum Computing?

---

## 📄 ArXiv Research Tool

The tutor can search research papers from ArXiv.

Examples:

* Latest research on LLMs
* Papers on Reinforcement Learning
* Research about Computer Vision

---

## 🧮 Calculator Tool

Supports mathematical calculations.

Examples:

* 25 * 30
* 500 / 25
* (45 + 20) * 3

---

## 📝 Learning Support Features

* Document Summarization
* Quiz Generation
* Flashcard Creation
* Context-Aware Learning
* Conversational Chat Interface

---

# 🏗️ System Architecture

User

↓

Streamlit Frontend

↓

Router

├── Document QA (RAG)

├── General Tutor

├── Wikipedia Tool

├── ArXiv Tool

└── Calculator Tool

↓

Groq LLM

↓

Response

---

# 🛠️ Tech Stack

## Frontend

* Streamlit

## LLM

* Groq
* Llama 3.3 70B Versatile

## Framework

* LangChain
* LangGraph

## Embeddings

* sentence-transformers/all-MiniLM-L6-v2

## Vector Database

* FAISS

## Tools

* Wikipedia API
* ArXiv API
* Calculator Tool

## File Processing

* PyPDF
* python-docx

---

# 📂 Project Structure

```text
EduSmart-AI-Tutor/

│
├── app.py
│
├── src/
│   │
│   ├── llm.py
│   ├── embeddings.py
│   ├── tools.py
│   ├── agents.py
│   ├── tutor.py
│   ├── memory.py
│   │
│   ├── doc_loader.py
│   ├── vector_store.py
│   └── retriever.py
│
├── uploads/
│
├── requirements.txt
│
├── .env
│
└── README.md
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone <repository_url>

cd EduSmart-AI-Tutor
```

## Create Virtual Environment

```bash
python -m venv tutor
```

### Windows

```bash
tutor\Scripts\activate
```

### Linux / Mac

```bash
source tutor/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 📦 Required Packages

```text
streamlit

langchain==0.3.25
langchain-core==0.3.59
langchain-community==0.3.24

langchain-groq
langchain-openai
langchain-huggingface

langgraph

faiss-cpu

sentence-transformers

pypdf

python-docx

python-dotenv
```

---

# 🔑 Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

---

# ▶️ Running the Application

```bash
streamlit run app.py
```

Application will launch at:

```text
http://localhost:8501
```

---

# 🧪 Example Queries

## Document Mode

* Summarize this document
* Explain chapter 3
* Generate quiz questions
* Create flashcards

## General Tutor Mode

* Explain Machine Learning
* What is Deep Learning?
* Difference between AI and ML

## Wikipedia Mode

* Who was Isaac Newton?
* History of India

## ArXiv Mode

* Latest transformer research papers
* Papers on Retrieval-Augmented Generation

## Calculator

* 120 * 45
* 5000 / 25

---

# 🔒 Privacy and Safety Considerations

This project is designed with educational use in mind.

Recommendations for production deployment:

* Encrypt uploaded files
* Implement authentication
* Restrict file access
* Add content moderation
* Store conversation history securely
* Comply with COPPA and GDPR requirements when working with minors

---

# 📈 Future Enhancements

* Voice-Based Tutor
* Multi-Language Support
* Personalized Learning Paths
* Student Progress Tracking
* Teacher Dashboard
* LangGraph Agent Workflows
* Persistent Memory with PostgreSQL
* Vector Database Migration (Chroma / Pinecone)
* Study Planner Agent
* Career Guidance Agent

---

# 🎯 Learning Objectives

This project demonstrates:

* Retrieval-Augmented Generation (RAG)
* LangChain Pipelines
* Tool Calling
* Vector Search
* Educational AI Systems
* Conversational Interfaces
* LLM Integration
* Agent-Based Workflows
* Streamlit Deployment

---

# 👨‍💻 Author

Built as a Generative AI Engineering project focused on creating intelligent, personalized, and scalable educational assistants using modern LLM and RAG architectures.
