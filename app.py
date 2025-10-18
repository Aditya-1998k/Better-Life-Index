from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

# Loading the Trained model
model = joblib.load("better_life_model.pkl")


AVERAGE_BLI = 6.5 # calculated

app = FastAPI(title="Better Life Index Predictor")


class InputData(BaseModel):
    country: str
    gdp_per_capita: float


@app.get("/")
def read_root():
    return {"message": "Welcome to Better Life Index API"}


@app.post("/predict")
def predict(data: InputData):
    """
    This API will accept country name
    and GDP per capita and return
    Better life index along with comparison
    with other countries
    """
    x = pd.DataFrame([[data.gdp_per_capita]], columns=["GDP per capita (USD)"])
    prediction = model.predict(x)[0]

    comparison = (
        "better than average" if prediction > AVERAGE_BLI else "worse than average"
    )

    response = {
        "country": data.country,
        "better_life_index": round(prediction, 2),
        "comparison": comparison,
    }
    return response

