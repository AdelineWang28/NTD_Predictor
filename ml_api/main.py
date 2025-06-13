# ml_api/main.py
from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI()

class PredictRequest(BaseModel):
    region: str
    year: int

@app.post("/predict")
def predict_outbreak(data: PredictRequest):
    """
    Simulated ML model — returns random 0 or 1.
    """
    return {
        "region": data.region,
        "year": data.year,
        "outbreak": int(random.random() > 0.5)
    }
