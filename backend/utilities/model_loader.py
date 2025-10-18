import os
import joblib
from utilities.logging_config import get_logger

logger = get_logger("model_loader")

def load_model(model_filename: str = "better_life_model.pkl"):
    """
    Load a trained model from the models directory.
    Returns the model object.
    """
    base_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(base_dir, "..", "models", model_filename)

    if not os.path.exists(model_path):
        logger.error(f"Model file not found: {model_path}")
        raise FileNotFoundError(f"Model file not found: {model_path}")

    model = joblib.load(model_path)
    logger.info(f"Model loaded from {model_path}")
    return model

