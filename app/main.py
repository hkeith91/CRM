from fastapi import FastAPI, HTTPException
from .models.contact import Contact
from typing import List
import uuid

app = FastAPI()


# A temporary db for testing
contact_db: List[Contact] = []


@app.get("/")
async def hello_world():
    """
    This function handles GET requests to the root URL.
    Returns a simple JSON response
    """
    return {"message": "Hello World!"}
