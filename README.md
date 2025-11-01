## Crypto Whitepaper Chatbot

A **Retrieval-Augmented Generation (RAG)** powered chatbot that allows users to **chat with any cryptocurrency whitepaper**.
Built using **LangChain**, **Milvus**, **Groq**, **Gemini**, and a complete end-to-end pipeline for document ingestion, embedding, and query generation.

**Live App:** [https://llm-powered-crypto-whitepaper-chatbot.streamlit.app/](https://llm-powered-crypto-whitepaper-chatbot.streamlit.app/)

---

### Key Features

- Automatic whitepaper scraping – fetches the latest whitepaper from the web using the coin name
- PDF loader and text splitter – extracts and prepares text for embedding
- Embedding and vector database (Milvus) – stores semantic representations for retrieval
- LLM-powered generation – produces accurate answers using context from the whitepaper
- Streamlit frontend – clean and interactive web interface
- Automatic cleanup – clears temporary data after each query

---

### Tech Stack

| Component    | Technology                      |
| ------------ | ------------------------------- |
| Frontend     | Streamlit                       |
| LLM          | Groq API, Gemini API            |
| Vector Store | Milvus                          |
| Embeddings   | LangChain, SentenceTransformers |
| Pipeline     | Python (OOP-based modules)      |
| Logging      | Custom Logger (`src.logging`)   |

---

### Architecture Flow

```
User Input → Scraper → PDF Loader → Text Splitter → Embedding → Vector DB → Groq Generation → Streamlit Display
```

---

### Streamlit UI Preview

<img width="1905" height="905" alt="App Preview" src="https://github.com/user-attachments/assets/20b37355-d3fe-4d74-b29c-6fa16d9c0577" />

```bash
streamlit run app.py
```

**UI Features:**
- Enter coin name (e.g., Bitcoin, Ethereum)
- Ask any question about the selected whitepaper
- Adjust temperature for response creativity
- View live progress (scraping → embedding → answering)
- Automatic cleanup after response generation

---

### Setup & Installation

**Step 1: Clone the repository**

```bash
git clone https://github.com/AyushAI14/Crypto-Whitepaper-Chatbot.git
cd Crypto-Whitepaper-Chatbot
```

**Step 2: Install dependencies**

```bash
pip install -r requirements.txt
```

**Step 3: Run the app**

```bash
streamlit run app.py
```

---

### Configuration

Set your API keys inside the `.env` file or in `Generation.py`

```python
os.getenv("GROQ_API_KEY")
os.getenv("GEMINI_API_KEY")
```

---

### Cleanup Logic

After each query:
- `db.clear_store()` – clears the vector database
- `scraper.clear_whitepapers()` – removes temporary whitepapers
- `l.clear_raw_txt()` – deletes raw text files

This ensures a clean environment for every run.

---

### Author

**Developed by [Ayush Vishwakarma](https://github.com/AyushAI14)**


---