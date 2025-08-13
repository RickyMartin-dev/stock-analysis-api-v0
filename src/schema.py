from pydantic import BaseModel, Field

class PredictIn(BaseModel):
    ticker: str = Field(..., pattern=r"^[A-Z.]{1,10}$")

class PredictOut(BaseModel):
    ticker: str
    prob_up: float
    will_close_up: int
    model_version: str