import streamlit as st
from src.loaders.scraping import WhitepaperScaper
from src.loaders.loader import Loader
from src.embeddings.Embed import EmbeddingChunker
from src.vector_store.MilvusDB import Vectordb
from src.llm.Generation import Generation
from src.logging import logger

# ---------------- Streamlit UI Setup ----------------
st.set_page_config(page_title="Crypto Whitepaper Chatbot", page_icon="🪙", layout="wide")

st.markdown("<h1 style='text-align: center; color: gold;'>🪙 Crypto Whitepaper Chatbot</h1>", unsafe_allow_html=True)
st.markdown("<h3>Analyze and chat with cryptocurrency whitepapers — powered by your RAG pipeline.</h3>", unsafe_allow_html=True)


st.divider()

# ---------------- Input Section ----------------
coin_name = st.text_input("🔍 Enter Coin Name", placeholder="e.g. Bitcoin, Ethereum, Solana")

col1, col2 = st.columns([1, 3])
with col1:
    temperature = st.slider("🔥 Temperature", 0.0, 1.5, 0.8, 0.1)
with col2:
    user_query = st.text_input("💬 Ask a question about the whitepaper", placeholder="e.g. What is Bitcoin’s consensus mechanism?")

run_button = st.button("🚀 Run Pipeline & Generate Answer")

# ---------------- Main Logic ----------------
if run_button:
    if not coin_name:
        st.warning("⚠️ Please enter a coin name.")
        st.stop()

    with st.spinner(f"🔄 Scraping {coin_name} whitepaper..."):
        logger.info(f"Coin name entered: {coin_name}")
        scaper = WhitepaperScaper()
        scaper.CoinRetreiver(coin_name)
        logger.info(f"Scraping process for {coin_name} completed")

    with st.spinner("📄 Loading document..."):
        l = Loader()
        l.txt_splitter("Data/whitepapers")
        logger.info("Completed Loader process")

    with st.spinner("🔢 Creating embeddings..."):
        embedder = EmbeddingChunker()
        embedder.Embedding()
        logger.info("Completed Embedding process")

    with st.spinner("🧠 Populating Vector DB..."):
        db = Vectordb()
        splits = embedder.txt_splitter()
        db.add_Document(splits)
        logger.info("Completed VectorDB process")

    with st.spinner("⚡ Generating answer..."):
        g = Generation()
        answer = g.groq(user_query, temperature)
        st.success("✅ Generation completed!")
        st.markdown(f"### 🧩 **Answer:**\n{answer}")

    # ---------------- Cleanup Section ----------------
    with st.spinner("🧹 Cleaning temporary files..."):
        db.clear_store()
        scaper.clear_whitepapers()
        l.clear_raw_txt()
        logger.info("Cleanup completed")

    st.balloons()

st.divider()
st.markdown(
    """
    <p style='text-align: center; color: grey;'>
        Built By Ayush Vishwakarma by <a href='https://github.com/AyushAI14/LLM-Powered-Crypto-Whitepaper-Chatbot' target='_blank' style='text-decoration: none; color: gold; font-weight: bold;'>
        Github</a>
    </p>
    """,
    unsafe_allow_html=True
)
