from fastapi import APIRouter
from src.schemas.schema_cardsid import CardsID
from src.ml.predictor import predict, dict_to_df, load_model
from src.databases.mongodb_dml import read_from_mongodb
from src.utils.config import MONGODB_COLLECTION, MODEL_FILE_NAME
router = APIRouter()

@router.post("/predict")
async def post_predict(data: CardsID):
    """
        Post for Prediction
        args:
            id - Card ID
        Will return the Strategy
    """
    model = load_model(MODEL_FILE_NAME)

    data_enrich = read_from_mongodb(MONGODB_COLLECTION, data.id)
    df = dict_to_df(data_enrich)

    predict_result = predict(df, model)
    return predict_result
