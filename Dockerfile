FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    libffi-dev \
    libssl-dev \
    python3-dev \
    sqlite3 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
COPY setup.py .

RUN pip install --upgrade pip

RUN pip install "numpy<2"

RUN pip install --no-cache-dir "pymilvus[milvus_lite]"

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py"]
