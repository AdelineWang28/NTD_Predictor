from fastapi import FastAPI
from pydantic import BaseModel
from ml_api.main import predict

app = FastAPI()

class PredictRequest(BaseModel):
    region: str
    year: int
    features: list  # 示例：[32.1, 85.0, 1, 0, 0.75]

@app.post("/predict")
def predict_outbreak(data: PredictRequest):
    result = predict(data.region, data.year, data.features)
    return {
        "region": data.region,
        "year": data.year,
        "outbreak": result  # 预测结果 0 或 1
    }
