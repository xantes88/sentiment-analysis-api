# Step 1: Usa un'immagine di base ufficiale di Python
FROM python:3.8-slim

# Step 2: Imposta la directory di lavoro
WORKDIR /app

# Step 3: Copia i file di requisiti per installare le dipendenze
COPY sentiment_analysis/requirements.txt /app/

# Step 4: Installa le dipendenze
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copia il codice dell'app nella directory di lavoro
COPY sentiment_analysis /app/

# Step 6: Esponi la porta su cui FastAPI sarà in ascolto
EXPOSE 80

# Step 7: Definisci il comando per eseguire FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
