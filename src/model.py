import pandas as pd
from sklearn.linear_model import LinearRegression

def train_model(data_path: str) -> LinearRegression:
    # Load data from CSV
    df = pd.read_csv(data_path)
    
    # Basic train/test split
    X = df[['feature']]
    y = df['target']
    
    # Train a simple linear regression model
    model = LinearRegression().fit(X, y)
    
    return model
