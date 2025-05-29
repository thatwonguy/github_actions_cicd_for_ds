import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib  # For saving models

def train_model(data_path: str, output_path: str = "outputs/model.pkl") -> LinearRegression:
    # Load CSV into DataFrame
    df = pd.read_csv(data_path)
    
    # Extract features and target
    X = df[['feature']]
    y = df['target']
    
    # Train the model
    model = LinearRegression().fit(X, y)
    
    # Save the model to disk
    joblib.dump(model, output_path)
    
    return model
