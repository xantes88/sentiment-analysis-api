# Usa l'immagine base Python
FROM python:3.8-slim

# Imposta la directory di lavoro all'interno del container
WORKDIR /app

# Copia il file requirements.txt dalla cartella sentiment_analysis
COPY sentiment_analysis/requirements.txt .

# Installa le dipendenze
RUN pip install -r requirements.txt

# Copia tutto il codice del repository nella directory di lavoro
COPY . .

# Imposta il comando di esecuzione dell'app con Uvicorn
CMD ["uvicorn", "sentiment_analysis.main:app", "--host", "0.0.0.0", "--port", "80"]
