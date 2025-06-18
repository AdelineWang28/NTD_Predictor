from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# 输入数据模型
class PredictRequest(BaseModel):
    country: str
    year: int

# POST 接口用于接收预测请求
@app.post("/predict")
def predict(req: PredictRequest):
    # 🚧 暂时返回模拟预测值
    return {
        "country": req.country,
        "year": req.year,
        "outbreak": True,
        "confidence": 0.91
    }
