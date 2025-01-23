from fastapi import FastAPI
from prometheus_client import Counter, generate_latest, REGISTRY
from transformers import pipeline
from fastapi.responses import Response
import torch

# Verifica la disponibilità della GPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Crea l'app FastAPI
app = FastAPI()

# Carica il modello pre-addestrato per l'analisi del sentiment
sentiment_analysis = pipeline("sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment-latest", device=0 if torch.cuda.is_available() else -1)

# Contatori Prometheus
SENTIMENT_ANALYSIS_COUNT = Counter("sentiment_analysis_count", "Number of sentiment analyses performed")
SENTIMENT_LABEL_COUNT = Counter("sentiment_label_count", "Count of sentiment labels", ["label"])

# Endpoint root
@app.get("/")
async def root():
    return {"message": "Welcome to the Sentiment Analysis API!"}

# Endpoint per l'analisi del sentiment
@app.get("/sentiment/")
async def get_sentiment(text: str = "I love machine learning"):
    # Analisi del sentiment
    result = sentiment_analysis(text)
    
    # Incremento dei contatori
    SENTIMENT_ANALYSIS_COUNT.inc()  
    SENTIMENT_LABEL_COUNT.labels(label=result[0]['label']).inc()

    return {"sentiment": result[0]['label'], "score": result[0]['score']}

# Endpoint per le metriche di Prometheus
@app.get("/metrics/")
async def metrics():
    return Response(generate_latest(REGISTRY), media_type="text/plain")
    
