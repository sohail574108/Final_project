# 🎥 YouTube RAG Q&A Bot

> An AI-powered question-answering system that extracts knowledge from YouTube videos using Retrieval-Augmented Generation (RAG), LangGraph, Pinecone, and GPT-4o-mini.

---

## 📌 Project Overview

This project develops an intelligent RAG-based chatbot that enables users to ask natural language questions about YouTube video content. The system transcribes YouTube videos, indexes the content into a vector database, and uses a LangGraph ReAct agent to retrieve and answer user queries accurately — all through an interactive Gradio interface.

---

## 🎯 Objectives

- Extract and transcribe textual content from YouTube videos
- Index video transcripts into a Pinecone vector store for semantic search
- Answer user questions using a LangGraph ReAct agent powered by GPT-4o-mini
- Evaluate response quality using RAGAS metrics
- Trace and monitor all LLM interactions via LangSmith
- Provide a clean, interactive UI through Gradio

---

## 🏗️ Architecture

```
User Query
    │
    ▼
Gradio UI
    │
    ▼
LangGraph ReAct Agent (GPT-4o-mini)
    │
    ├──► Pinecone Vector Store ◄── YouTube Transcript Chunks
    │         (Semantic Retrieval)
    │
    ▼
Generated Answer + Retrieved Sources
    │
    ▼
LangSmith Tracing    RAGAS Evaluation
```

---

## 🧰 Tech Stack

| Component | Technology |
|---|---|
| LLM | GPT-4o-mini (OpenAI) |
| Agent Framework | LangGraph ReAct |
| Vector Store | Pinecone |
| Embeddings | text-embedding-3-small (OpenAI) |
| Transcript Extraction | YouTube Transcript API |
| Evaluation | RAGAS 0.4.x |
| Tracing & Monitoring | LangSmith |
| UI | Gradio 6.x |
| Language | Python 3.10+ |

---

## 📁 Project Structure

```
├── Final_Files/                  # Raw transcript text files
│   ├── f1.txt
│   ├── f2.txt
│   └── ...
├── notebooks/
│   ├── 01_ingestion.ipynb        # Transcript extraction & chunking
│   ├── 02_indexing.ipynb         # Pinecone vector store setup
│   ├── 03_agent.ipynb            # LangGraph ReAct agent
│   ├── 04_evaluation.ipynb       # RAGAS evaluation
│   └── 05_gradio_app.ipynb       # Gradio UI deployment
├── requirements.txt
├── .env
└── README.md
```

---

## ⚙️ Setup & Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/youtube-rag-bot.git
cd youtube-rag-bot
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # macOS/Linux
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=your_openai_api_key
PINECONE_API_KEY=your_pinecone_api_key
PINECONE_INDEX_NAME=your_index_name
LANGSMITH_API_KEY=your_langsmith_api_key
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=ragas-rag-eval
```

---

## 🚀 Usage

### Run the Gradio App

```bash
# Launch the interactive chatbot UI
python app.py
```

The app will start locally and provide a public shareable link via Gradio.

### Example Questions

- *"What is a hidden layer in neural networks?"*
- *"How does backpropagation work?"*
- *"What is gradient descent?"*
- *"Explain activation functions."*
- *"What is a neural network?"*

---

## 📊 RAGAS Evaluation

The system is evaluated using four RAGAS metrics:

| Metric | Description |
|---|---|
| **Faithfulness** | Are answers factually grounded in the retrieved context? |
| **Answer Relevancy** | How relevant is the answer to the question asked? |
| **Context Precision** | How precise is the retrieved context to the question? |
| **Context Recall** | Does the retrieved context cover the ground truth answer? |

Run the evaluation notebook to generate scores:

```bash
jupyter notebook notebooks/04_evaluation.ipynb
```

---

## 🔍 LangSmith Tracing

All LLM interactions are automatically traced to LangSmith for monitoring and debugging.

- **Project:** `ragas-rag-eval`
- **Dashboard:** [https://smith.langchain.com](https://smith.langchain.com)

Tracing is enabled via environment variables — no code changes needed.

---

## 📋 Requirements

```
openai
langchain
langchain-openai
langgraph
pinecone-client
youtube-transcript-api
ragas==0.4.3
gradio==6.9.0
langsmith
datasets
numpy
python-dotenv
```

---

## 🔮 Future Improvements

- Support for multiple YouTube videos via URL input
- Real-time transcript fetching from any YouTube URL
- Conversational memory across multi-turn sessions
- Support for multilingual video transcripts
- Fine-tuned embeddings on domain-specific content
- Automated RAGAS evaluation pipeline on new data

---

## 🤝 Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements.



---

## 👤 Author

**Sohail Hiraj**  
Final Project — AI/ML Lab  
📧 sohailhiraj08@gmail.com  
🔗 [GitHub](https://github.com/sohail574108)
