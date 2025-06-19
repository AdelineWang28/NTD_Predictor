import xgboost as xgb
import numpy as np

# load XGBoost 模型
booster = xgb.Booster()
booster.load_model("ml_api/xgb_model.json")  

# define predict function
def predict(region, year, features):
    """
    region/year 可用于记录；features 是特征值数组，如 [32.1, 85.0, 1, 0, 0.75]
    返回 0 或 1
    """
    dmatrix = xgb.DMatrix(np.array([features]))
    prediction = booster.predict(dmatrix)
    return int(prediction[0] > 0.5)  # 假设是二分类任务
