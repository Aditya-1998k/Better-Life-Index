from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import json

# local imports
from utilities.model_loader import load_model
from utilities.logging_config import get_logger
from utilities.rmq_utils import publish_to_rabbimq

logger = get_logger("backend")
regression_model = load_model('better_life_model_linear_regression.pkl')
kmeans_model = load_model('better_life_model_kmeans.pkl')
# Average BLI for comparison
AVERAGE_BLI = 6.5

app = FastAPI(title="Better Life Index API")


class InputData(BaseModel):
    country: str
    gdp_per_capita: float
    email: str


@app.get("/")
def read_root():
    return {"message": "Welcome to Better Life Index API. Please use /predict for Prediction"}


@app.post("/predict")
def predict(data: InputData):
    """
    Predicting the Better life index 
    of a country based on GDP per capita
    wrt to global data and 3 nearest neibour
    """
    try:
        x = pd.DataFrame([[data.gdp_per_capita]], columns=["GDP per capita (USD)"])
        linear_prediction = regression_model.predict(x)[0]
        kmeans_prediction = kmeans_model.predict(x)[0]
        
        prediction = linear_prediction if linear_prediction > kmeans_prediction else kmeans_prediction
        comparison = (
            "better than average" if prediction > AVERAGE_BLI else "worse than average"
        )

        logger.info(f"Prediction for {data.country}: {linear_prediction:.2f} with linear regression model.")
        logger.info(f"Prediction for {data.country}: {kmeans_prediction:.2f} with kmeans cluster model.")
        
        payload = {
            "user_email": data.email,
            "country": data.country,
            "better_life_index with with Global data (linear regression_model)": round(linear_prediction, 2),
            "better_life_index wrt 3 nearest neibour (kmeans cluster model)": round(kmeans_prediction, 2),
            "comparison": comparison,
        }
        publish_to_rabbimq("ml_queue", json.dumps(payload))
        return payload
    except Exception as e:
        logger.error(f"Prediction error: {e}")
        return {"error": "Prediction failed", "details": str(e)}
