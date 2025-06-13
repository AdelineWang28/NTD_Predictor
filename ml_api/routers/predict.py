from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

# define the input format of data
class InputData(BaseModel):
    feature1: float
    feature2: float

@router.post("/predict/")
async def predict(data: InputData):
    # call the model prediction function here
    return {
        "message": "model is not implemented yet",
        "input": data.dict()
    }
