from src.model import train_model
import os

def test_train_model():
    # Ensure the model trains without error
    model = train_model("data/sample.csv")
    assert model is not None
    assert hasattr(model, "predict")
