from src.logging import logger
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from dotenv import load_dotenv
from langchain_community.embeddings import HuggingFaceEmbeddings
import warnings
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=DeprecationWarning)


load_dotenv()



class EmbeddingChunker:
    def __init__(self):
        self.loader = TextLoader("Data/raw_loader/loader_text.txt")
        self.documents = self.loader.load()
        self.embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

        
    def txt_splitter(self):
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,  
            chunk_overlap=200,  
            add_start_index=True
        )
        all_splits = text_splitter.split_documents(self.documents)
        print(f"Splitting text file into {len(all_splits)} sub-documents.")
        return all_splits
    
    def Embedding(self):
        chunks = self.txt_splitter()
        
        logger.info("Generating embeddings for chunks...")
        vectors = self.embeddings.embed_documents([chunk.page_content for chunk in chunks])

        logger.info(f"Generated {len(vectors)} embeddings of dimension {len(vectors[0])}.")
        return vectors
        
# if __name__ == "__main__":
#     embedder = EmbeddingChunker()
#     vectors = embedder.Embedding()
#     print(f"✅ Successfully generated {len(vectors)} embeddings.")
#     print(f"Sample vector (first 10 values): {vectors[0][:10]}")
