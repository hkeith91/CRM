from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import uuid

app = FastAPI()


@app.get("/")
async def hello_world():
    """
    This function handles GET requests to the root URL.
    Returns a simple JSON response
    """
    return {"message": "Hello World!"}
