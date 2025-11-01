import streamlit as st
from src.loaders.scraping import WhitepaperScaper
from src.loaders.loader import Loader
from src.embeddings.Embed import EmbeddingChunker
from src.vector_store.MilvusDB import Vectordb
from src.llm.Generation import Generation
from src.logging import logger


# ---------------- Streamlit UI Setup ----------------
st.set_page_config(
    page_title="Crypto Whitepaper Chatbot",
    page_icon=None,
    layout="wide"
)

st.markdown("<h1 style='text-align: center; color: gold;'>Crypto Whitepaper Chatbot</h1>", unsafe_allow_html=True)
st.markdown("<h3>Analyze and interact with cryptocurrency whitepapers using a complete RAG pipeline.</h3>", unsafe_allow_html=True)
st.divider()


# ---------------- Input Section ----------------
coin_name = st.text_input("Enter Coin Name", placeholder="e.g. Bitcoin, Ethereum, Solana")

col1, col2 = st.columns([1, 3])
with col1:
    temperature = st.slider("Model Temperature", 0.0, 1.5, 0.8, 0.1)
with col2:
    user_query = st.text_input("Ask a Question", placeholder="e.g. What is Bitcoin’s consensus mechanism?")

run_button = st.button("Run Pipeline and Generate Answer")


# ---------------- Main Logic ----------------
if run_button:
    if not coin_name:
        st.warning("Please enter a coin name.")
        st.stop()

    # Step 1: Scrape whitepaper
    with st.spinner(f"Scraping {coin_name} whitepaper..."):
        logger.info(f"Coin name entered: {coin_name}")
        scaper = WhitepaperScaper()
        scaper.CoinRetreiver(coin_name)
        logger.info(f"Scraping completed for {coin_name}")

    # Step 2: Load and split text
    with st.spinner("Loading document..."):
        l = Loader()
        l.txt_splitter("Data/whitepapers")
        logger.info("Document loading completed")

    # Step 3: Create embeddings
    with st.spinner("Creating embeddings..."):
        embedder = EmbeddingChunker()
        embedder.Embedding()
        logger.info("Embedding process completed")

    # Step 4: Populate vector database
    with st.spinner("Populating vector database..."):
        db = Vectordb()
        splits = embedder.txt_splitter()
        db.add_Document(splits)
        logger.info("Vector database update completed")

    # Step 5: Generate answer
    with st.spinner("Generating answer..."):
        g = Generation()
        answer = g.groq(user_query, temperature)
        st.success("Response generated successfully.")
        st.markdown(f"### Answer:\n{answer}")

    # Step 6: Cleanup temporary files
    with st.spinner("Cleaning temporary files..."):
        db.clear_store()
        scaper.clear_whitepapers()
        l.clear_raw_txt()
        logger.info("Cleanup completed")

    st.balloons()


# ---------------- Footer ----------------
st.divider()
st.markdown(
    """
    <p style='text-align: center; color: grey;'>
        Built by Ayush Vishwakarma
        <a href='https://github.com/AyushAI14/LLM-Powered-Crypto-Whitepaper-Chatbot'
        target='_blank' style='text-decoration: none; color: gold; font-weight: bold;'>
        GitHub
        </a>
    </p>
    """,
    unsafe_allow_html=True
)
