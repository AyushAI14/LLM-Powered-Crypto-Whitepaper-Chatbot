
---

## 🪙 Crypto Whitepaper Chatbot

A **Retrieval-Augmented Generation (RAG)** powered chatbot that lets you **chat with any cryptocurrency whitepaper**.
Built using **LangChain**, **Milvus**, **Groq**,**Gemini** and a full end-to-end pipeline for document ingestion, embedding, and query generation.

---

### 🚀 Features

- ✅ **Automatic Whitepaper Scraping** — Fetches the latest whitepaper from the web using the coin name 
- ✅ **PDF Loader & Text Splitter** — Extracts and prepares text for embedding
- ✅ **Embedding + Vector Database (Milvus)** — Stores semantic representations for retrieval
- ✅ **LLM Generation** — Fast, high-quality answers using context from the whitepaper
- ✅ **Streamlit Frontend** — Simple, elegant, and interactive UI
- ✅ **Automatic Cleanup** — Clears whitepapers, text files, and vector DB after each query

---

### 🧩 Tech Stack

| Component    | Technology                           |
| ------------ | ------------------------------------ |
| Frontend     | **Streamlit**                        |
| LLM          | **Groq API , Gemini API**       |
| Vector Store | **Milvus**                           |
| Embeddings   | **LangChain + SentenceTransformers** |
| Pipeline     | **Python OOP Modules**               |
| Logging      | **Custom Logger (`src.logging`)**    |

---

### 🧠 Architecture Flow

```
User Input → Scraper → PDF Loader → Text Splitter → Embedding → Vector DB → Groq Generation → Streamlit Display
```

---



---

### 🖥️ Streamlit UI Preview

<img width="1905" height="905" alt="Image" src="https://github.com/user-attachments/assets/20b37355-d3fe-4d74-b29c-6fa16d9c0577" />

```python
streamlit run app.py
```

**Features in UI:**

* 🔍 Enter coin name (e.g., Bitcoin, Ethereum)
* 💬 Ask any question about its whitepaper
* 🔢 Adjust temperature for creativity
* ⚡ Live progress indicators (scraping → embedding → answer)
* 🎉 Auto cleanup after generation

---

### ⚙️ Setup & Installation

#### 1 Clone the repo

```bash
git clone https://github.com/AyushAI14/Crypto-Whitepaper-Chatbot.git
cd Crypto-Whitepaper-Chatbot
```

#### 2 Install dependencies

```bash
pip install -r requirements.txt
```

#### 3 Run the app

```bash
streamlit run app.py
```

---

### 🔧 Configuration

Update your **Groq API key** or other environment variables inside `.env` or within `Generation.py`:

```bash
os.getenv("GROQ_API_KEY")
os.getenv("GEMINI_API_KEY")
```

---

### 🧹 Cleanup Logic

After every query:

* 🗑️ `db.clear_store()` — clears vector DB
* 📄 `scaper.clear_whitepapers()` — removes temp whitepapers
* 📃 `l.clear_raw_txt()` — deletes raw text

Ensures a clean, fresh environment for each run.

---

### 🧑‍💻 Author

**Built by [Ayush Vishwakarma](https://github.com/AyushAI14)**

---

### ⭐ Future Improvements

* coins list

---

