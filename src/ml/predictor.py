import joblib
import pandas as pd
from functools import lru_cache
from sklearn.pipeline import Pipeline

@lru_cache
def load_model(model_path: str) -> Pipeline:
    """
        Load Model based
    """
    return joblib.load(model_path)

def dict_to_df(data: dict) -> pd.DataFrame:
    """
        Take a dictonary and tranform to a pandas data frame
        args:
            data
    """
    return pd.DataFrame(data, index=[0])

def predict(data: pd.DataFrame, model: Pipeline) -> str:
    """"
        Score the data using Model.pkl
        data: pd.DataFrame

        return str: that contain early or early strategy
    """
    
    prediction = model.predict(data)
    return str(prediction[0])
