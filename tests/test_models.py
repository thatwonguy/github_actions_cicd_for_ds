from src.model import train_model
import os

def test_train_model():
    # Train the model and save it
    model = train_model("data/sample.csv", "outputs/model.pkl")
    
    # Assert model is trained
    assert model is not None
    assert hasattr(model, "predict")
    
    # Check if model file exists
    assert os.path.exists("outputs/model.pkl")
