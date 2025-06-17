from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI()

class PredictionRequest(BaseModel):
    country: str
    year: int

@app.post("/predict")
def predict_outbreak(data: PredictionRequest):
    # Simulate prediction logic
    outbreak = random.choice([0, 1])
    confidence = round(random.uniform(0.75, 0.95), 2)

    return {
        "country": data.country,
        "year": data.year,
        "outbreak": outbreak,
        "confidence": confidence
    }
