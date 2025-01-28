from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline

# Inizializza l'app FastAPI
app = FastAPI(title="Sentiment Analysis API", version="1.0")

# Inizializza il modello HuggingFace
sentiment_model = pipeline("sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment-latest")

# Definizione del payload di input
class SentimentRequest(BaseModel):
    text: str

# Endpoint di esempio: root
@app.get("/")
def read_root():
    return {"message": "Welcome to the Sentiment Analysis API!"}

# Endpoint per analizzare il sentiment
@app.post("/analyze-sentiment/")
def analyze_sentiment(request: SentimentRequest):
    try:
        result = sentiment_model(request.text)
        return {"input_text": request.text, "sentiment": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))