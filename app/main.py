from fastapi import FastAPI

from app.routers import encode_decode


app = FastAPI()

app.include_router(encode_decode.router)