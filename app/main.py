import json

import sentry_sdk
from fastapi import FastAPI, HTTPException, Response, status
from sentry_sdk.integrations.asgi import SentryAsgiMiddleware

from app.models import *
from .routers import notes, trump, jokes

# load config
with open("config.json", "r") as f:
    config = json.load(f)

app = FastAPI(
    title="api.crrapi.xyz",
    version="0.0.1"
)

for router_module in (notes, trump, jokes):
    app.include_router(router_module.router)

if sentry_dsn := config.get("sentry_dsn"):
    sentry_sdk.init(
        dsn=sentry_dsn,
        traces_sample_rate=1.0,
    )
    app.add_middleware(SentryAsgiMiddleware)

@app.get("/")
async def index():
    return {"message": "Hello World"}
