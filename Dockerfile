FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
COPY setup.py .


RUN pip install --no-cache-dir  requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py"]