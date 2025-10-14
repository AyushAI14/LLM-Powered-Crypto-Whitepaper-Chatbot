from src.logging import logger
from langchain_community.document_loaders import PyMuPDFLoader,DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os

class Loader:
    def __init__(self):
        os.makedirs("Data/raw_loader/", exist_ok=True)
        
    def directory_loader(self):
        try:
            logger.info('directory_loader has been Intialized')
            dirload  = DirectoryLoader(
                path='Data/whitepapers/',
                glob='**/*.pdf',
                loader_cls=PyMuPDFLoader
            )
            dir_docs = dirload.load()
            
            return dir_docs
        except Exception as e:
            print(f"Unable to load to directory {e}")
            
    def txt_splitter(self):
        try:
            text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=1000,  
                chunk_overlap=200,  
                add_start_index=True
            )
            
            all_splits = text_splitter.split_documents(self.directory_loader)
            print(f"Splitting text file into {len(all_splits)} sub-documents.")
            all_text = "\n\n".join([all_splits[i].page_content for i in range(0,len(all_splits))])
            path = f"Data/raw_loader/loader_text.txt"
            with open(path, "w") as f:
                f.write(all_text)
            logger.info(f'files has been written successfully on {path}')
        except Exception as e:
            print(f"Unable to split text file {e}")
