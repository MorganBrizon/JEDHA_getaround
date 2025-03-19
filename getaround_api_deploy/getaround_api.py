from fastapi import FastAPI
import uvicorn
import numpy as np
import pandas as pd
from pydantic import BaseModel
from sklearn.pipeline import Pipeline
import joblib

# Charger le modèle entraîné
model = joblib.load("getaround_pricing_model.pkl")

# Définition de l'API FastAPI
app = FastAPI()

# Définition du format des entrées
class CarFeatures(BaseModel):
    mileage: int
    engine_power: int
    fuel: str
    paint_color: str
    car_type: str

# Endpoint de prédiction
@app.post("/predict")
def predict_price(features: CarFeatures):
    input_data = pd.DataFrame([features.dict()])
    prediction = model.predict(input_data)[0]
    return {"predicted_price": round(prediction, 2)}

# Lancer l'API (à exécuter uniquement en local)
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
