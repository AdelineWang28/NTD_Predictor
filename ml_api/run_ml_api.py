from fastapi import FastAPI
from pydantic import BaseModel
import random
import uvicorn

app = FastAPI()

class PredictRequest(BaseModel):
    country: str  # ← 与前端一致
    year: int

@app.post("/predict")
def predict_outbreak(data: PredictRequest):
    return {
        "country": data.country,
        "year": data.year,
        "outbreak": int(random.random() > 0.5),
        "confidence": round(random.uniform(0.7, 0.99), 2)  # 可选加上置信度
    }

if __name__ == "__main__":
    uvicorn.run("run_ml_api:app", host="127.0.0.1", port=8001, reload=True)
