from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import joblib, numpy as np

app = FastAPI(title="House Price Prediction API")
model = joblib.load('xgb_house_price_model.pkl')

class HouseInput(BaseModel):
    bedrooms: int
    bathrooms: int
    area: Optional[float] = None       # primary field used by eval script
    area_sqft: Optional[float] = None  # kept for backward compatibility
    age: Optional[int] = None          # accepted but not used by model

@app.get('/')
def root():
    return {'status': 'ok', 'message': 'House Price Prediction API'}

@app.get('/health')
def health():
    return {'status': 'healthy'}

@app.post('/predict')
def predict(data: HouseInput):
    # Resolve area: prefer 'area', fall back to 'area_sqft'
    resolved_area = data.area if data.area is not None else (data.area_sqft or 0.0)
    x = np.array([[data.bedrooms, data.bathrooms, resolved_area]])
    predicted_price = float(model.predict(x)[0])
    return {
        'predicted_price': predicted_price,
        'features_used': {
            'bedrooms': data.bedrooms,
            'bathrooms': data.bathrooms,
            'area': resolved_area,
            'age': data.age
        }
    }
