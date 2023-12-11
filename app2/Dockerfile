# app2/Dockerfile
FROM python:3.8

WORKDIR /app

# Kopiowanie plików aplikacji
COPY app2.py .
COPY requirements.txt .

# Instalacja zależności
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app2.py"]