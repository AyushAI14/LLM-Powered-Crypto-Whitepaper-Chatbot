from src.logging import logger
from langchain_community.document_loaders import PyMuPDFLoader,DirectoryLoader
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
            all_text = "\n\n".join([dir_docs[i].page_content for i in range(0,len(dir_docs))])
            path = f"Data/raw_loader/loader_text.txt"
            with open(path, "w") as f:
                f.write(all_text)
            logger.info(f'files has been written successfully on {path}')
            return dir_docs
        except Exception as e:
            print(f"Unable to load to directory {e}")
            