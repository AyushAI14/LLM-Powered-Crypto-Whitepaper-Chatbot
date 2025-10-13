import os 
from pathlib import Path
import logging

file_dir = 'src'

file_list = [
    f"{file_dir}/__init__.py",
    f"{file_dir}/utils/__init__.py",
    f"{file_dir}/utils/common.py",
    f"{file_dir}/logging/__init__.py",
    f"{file_dir}/pipeline/__init__.py",
    f"{file_dir}/loaders/__init__.py",
    f"{file_dir}/embeddings/__init__.py",
    f"{file_dir}/retrieval/__init__.py",
    f"{file_dir}/vector_store/__init__.py",
    f"{file_dir}/llm/__init__.py",
    "requirements.txt",
    "setup.py",
    "Data/__init__.py",
    "Data/raw_files",
    "app.py",
    "main.py",
    "Dockerfile",
]


try:
    for filepath in file_list:
        filepath = Path(filepath)
        filedir , filename = os.path.split(filepath)
        if filedir != '':
            os.makedirs(filedir,exist_ok=True)
        if (not os.path.exists(filepath) or (os.path.getsize==0)):
            with open(filepath,'w') as f:
                logging.info(f"----Creating file: {filepath}----")
                pass
except Exception as e:
    logging.info('Error occured while creating files',e)