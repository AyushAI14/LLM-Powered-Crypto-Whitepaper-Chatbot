from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from dotenv import load_dotenv
import os
load_dotenv()
google_api_key=os.getenv('GEMINI_API_KEY')
print(google_api_key)