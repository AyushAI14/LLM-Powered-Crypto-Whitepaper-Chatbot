from src.loaders.scraping import WhitepaperScaper
from src.loaders.loader import Loader
from src.logging import logger
from src.embeddings.Embed import EmbeddingChunker

coin_input = str(input("Enter the coin name : "))
logger.info(f"Coin name entered: {coin_input}")

# -- Scraping process started
logger.info(f"Starting scraping process for {coin_input}")
scaper = WhitepaperScaper()
scaper.CoinRetreiver(coin_input)
logger.info(f"Scraping process for {coin_input} completed")

# -- Loading document from pdf
logger.info(f"Starting Loader process --")
l = Loader()
l.directory_loader()
logger.info(f"Completed Loader process --")

# -- Embedding process started
logger.info(f"Starting Embedding process --")
embedder = EmbeddingChunker()
embedder.Embedding()
logger.info(f"Completed Embedding process --")
