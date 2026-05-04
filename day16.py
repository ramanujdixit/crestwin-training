from fastapi import FastAPI, Request, Response
from slowapi.util import get_remote_address
from slowapi import Limiter
from slowapi.errors import RateLimitExceeded
from fastapi.responses import JSONResponse
from html import escape
from pydantic import BaseModel

app = FastAPI()

limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter


class Message(BaseModel):
    text: str


@app.exception_handler(RateLimitExceeded)
async def rate_limit_handler(request: Request, exc: RateLimitExceeded):
    return JSONResponse(
        status_code=429,
        content={
            "error": "Rate limit exceeded",
            "detail": "Only 3 requests per minute allowed",
        },
    )


@app.get("/")
@limiter.limit("3/minute")
async def home(request: Request, response: Response):
    response.headers["Strict-Transport-Security"] = "max-age=31536000"
    response.headers["Content-Security-Policy"] = "default-src 'self'"
    return {"message": "welcome buddy"}


@app.post("/message")
async def message(data: Message):
    clean_text = escape(data.text)
    return {"cleaned_message": clean_text}
