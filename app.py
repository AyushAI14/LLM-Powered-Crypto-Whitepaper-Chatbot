from src.logging import logger
from langchain_community.document_loaders import PyMuPDFLoader,DirectoryLoader
import os

dirload  = DirectoryLoader(
    path='Data/whitepapers/',
    glob='**/*.pdf',
    loader_cls=PyMuPDFLoader
)
dir_docs = dirload.load()
all_text = "\n\n".join([dir_docs[i].page_content for i in range(0,len(dir_docs))])
print(len(dir_docs))
print(all_text)