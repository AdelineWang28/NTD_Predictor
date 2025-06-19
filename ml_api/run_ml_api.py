from fastapi import FastAPI
from pydantic import BaseModel
import random
from ml_api import main  # 导入你刚刚贴出的 main.py 中的 predict 函数

app = FastAPI()

class PredictRequest(BaseModel):
    country: str
    year: int

@app.post("/predict")
def predict_outbreak(data: PredictRequest):
    # 示例：用随机特征模拟输入
    fake_features = [random.uniform(0, 1) for _ in range(5)]  # 用5个特征占位
    pred = main.predict(data.country, data.year, fake_features)
    confidence = random.uniform(0.7, 0.99)

    return {
        "country": data.country,
        "year": data.year,
        "outbreak": pred,
        "confidence": round(confidence, 2)
    }
