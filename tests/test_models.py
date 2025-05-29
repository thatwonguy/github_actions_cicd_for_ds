from src.model import train_model
import os

def test_train_model():
    # Train model and save to outputs/
    model = train_model("data/sample.csv", "outputs/model.pkl")

    # Ensure model is created
    assert model is not None
    assert hasattr(model, "predict")

    # Ensure model file was saved
    assert os.path.exists("outputs/model.pkl")
