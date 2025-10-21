from src.loaders.scraping import WhitepaperScaper
from src.loaders.loader import Loader
from src.logging import logger
from src.embeddings.Embed import EmbeddingChunker
from src.vector_store.MilvusDB import Vectordb
from src.llm.Generation import Generation


# -- Scraping process started
coin_input = str(input("Enter the coin name : "))
logger.info(f"Coin name entered: {coin_input}")
logger.info(f"Starting scraping process for {coin_input}")
scaper = WhitepaperScaper()
scaper.CoinRetreiver(coin_input)
logger.info(f"Scraping process for {coin_input} completed")

# -- Loading document from pdf
logger.info(f"Starting Loader process --")
dirpath ='Data/whitepapers'
l = Loader()
l.txt_splitter(dirpath)
logger.info(f"Completed Loader process --")

# -- Embedding process started
logger.info(f"Starting Embedding process --")
embedder = EmbeddingChunker()
embedder.Embedding()
logger.info(f"Completed Embedding process --")

# -- VectorDB
logger.info(f"Starting VectorDB process --")
db = Vectordb()
splits = embedder.txt_splitter()
db.add_Document(splits)
# Result = db.query("What is Bitcoin's consensus mechanism?",2)
# print(Result)
logger.info(f"Completed VectorDB process --")

# skipping the vector db row because it is already running in generation process  but not all part is skipping

# --  Generation
logger.info(f"Starting Generation process --")

g = Generation()
temperature = 0.8
print(g.groq("What is Bitcoin ",temperature))
# print(g.gemini("What is Bitcoin ",temperature))
db.clear_store() # for clearing vecter db
scaper.clear_whitepapers()  #for clearing whitepaper
l.clear_raw_txt()  #for clearing raw text file
logger.info(f"Completed Generation process --")
