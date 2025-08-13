from fastapi import FastAPI, Request, HTTPException
from mangum import Mangum
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
from schema import PredictIn, PredictOut
from .rate_limit import limiter
from .clients import invoke_model
from .logging_setup import log_json
from .config import API_TITLE, API_VERSION

app = FastAPI(title=API_TITLE, version=API_VERSION)
app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)

@app.exception_handler(RateLimitExceeded)
async def rate_limit_handler(request: Request, exc: RateLimitExceeded):
    return HTTPException(status_code=429, detail="Rate limit exceeded")

@app.get('/health')
async def health():
    return {"ok": True}

@app.post('/predict', response_model=PredictOut)
async def predict(inp: PredictIn, request: Request):
    # (Optional) API key/JWT checks here
    res = invoke_model(inp.ticker)
    log_json(route="/predict", ticker=inp.ticker, prob=res['prob_up'])
    return res
    
handler = Mangum(app)