from fastapi import FastAPI
from dotenv import load_dotenv
import os
import socket
import logging
from prometheus_fastapi_instrumentator import Instrumentator

# Load environment variables from .env
load_dotenv()

# Create FastAPI app instance
app = FastAPI()

# Setup logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Instrumentator config
Instrumentator().instrument(app).expose(app)

@app.get("/")
def root():
    return {"message": "FastAPI app is running. Visit /get_info for full details."}

@app.get("/get_info")
def get_info():
    pod = socket.gethostname()
    logger.info(f"Handled by pod: {pod}")
    return {
        "APP_VERSION": os.getenv("APP_VERSION", "unknown"),
        "APP_TITLE": os.getenv("APP_TITLE", "default title"),
        "ENVIRONMENT": os.getenv("ENVIRONMENT", "development"),
        "AUTHOR": os.getenv("AUTHOR", "syed.m.haider"),
        "HOSTNAME": pod
    }