import pytest
import pandas as pd
import logging

from src.ml.predictor import predict

class TestPredictorModule:    
    def setUp():
        logging.info("Inicio test predictor")

    def test_predict_return(setUp):
        data = {
            "id":	1118	,
            "name": "Firewine",
            "mana": 5	,
            "attack": 0	,
            "health": 0	,
            "type": "spell"	,
            "god": "nature"
        }
        result_expect = ["late","early"]
        
        df= pd.DataFrame(data, index=[0])
        result_predict = predict(df)
        
        assert result_predict in result_expect

