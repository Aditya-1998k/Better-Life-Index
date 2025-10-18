from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import os

# local imports
from utilities.model_loader import load_model
from utilities.logging_config import get_logger

logger = get_logger("backend")
model = load_model()

# Average BLI for comparison
AVERAGE_BLI = 6.5

app = FastAPI(title="Better Life Index API")


class InputData(BaseModel):
    country: str
    gdp_per_capita: float


@app.get("/")
def read_root():
    return {"message": "Welcome to Better Life Index API"}


@app.post("/predict")
def predict(data: InputData):
    try:
        x = pd.DataFrame([[data.gdp_per_capita]], columns=["GDP per capita (USD)"])
        prediction = model.predict(x)[0]

        comparison = (
            "better than average" if prediction > AVERAGE_BLI else "worse than average"
        )

        logger.info(f"Prediction for {data.country}: {prediction:.2f}")

        return {
            "country": data.country,
            "better_life_index": round(prediction, 2),
            "comparison": comparison,
        }
    except Exception as e:
        logger.error(f"Prediction error: {e}")
        return {"error": "Prediction failed", "details": str(e)}
