from pydantic import BaseModel


class CardsID(BaseModel):
    id: int

    class Config:
        schema_extra = {
            "example": {
                "id":	1118
            }
        }
