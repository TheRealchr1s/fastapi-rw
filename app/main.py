import json

import sentry_sdk
from fastapi import FastAPI, HTTPException, Response, status
from fastapi.middleware.cors import CORSMiddleware
from sentry_sdk.integrations.asgi import SentryAsgiMiddleware

from app.models import *
from .routers import trump, jokes

# load config
with open("config.json", "r") as f:
    config = json.load(f)

app = FastAPI(
    title="api.crrapi.xyz",
    version="0.0.1"
)

if cors_origins := config.get("cors_origins"):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=cors_origins,
        allow_methods=["*"],
        allow_headers=["*"],
    )

for router_module in (trump, jokes):
    app.include_router(router_module.router)

if sentry_dsn := config.get("sentry_dsn"):
    sentry_sdk.init(
        dsn=sentry_dsn,
        traces_sample_rate=1.0,
        environment=config["sentry_environment"],
    )
    app.add_middleware(SentryAsgiMiddleware)

@app.get("/")
async def index():
    return {"message": "Hello World"}
