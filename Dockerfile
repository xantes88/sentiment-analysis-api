# Utilizza un'immagine Python di base
FROM python:3.8-slim

# Imposta la directory di lavoro
WORKDIR /app

# Copia il file di dipendenze
COPY requirements.txt .

# Installa le dipendenze
RUN pip install --no-cache-dir -r requirements.txt

# Copia il codice dell'app
COPY . .

# Espone la porta su cui l'app ascolta
EXPOSE 8000

# Comando per avviare l'app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
