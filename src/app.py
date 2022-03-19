from sys import prefix
import numpy as np
import pandas as pd
from fastapi import FastAPI
from src.routes.predict_strategy import router as router_strategy


app = FastAPI(
    title="Gods Unchained API",
    version="0.1",
    description="API para Classificar cards do Gods Unchained"
)


@app.get("/healthcheck", tags=["health"])
async def healthcheck():
    """
        Checks the API Health.
    """
    return {"status": "alive"}

app.include_router(router_strategy, tags=["Strategy Prediction"], prefix="/strategy_prediction")