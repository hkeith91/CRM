from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import uuid

app = FastAPI()


# This is a  comment to test the CI pipeline
class Contact(BaseModel):
    name: str
    email: str
    phone: Optional[str] = None
    company: Optional[str] = None


@app.get("/")
async def hello_world():
    """
    This function handles GET requests to the root URL.
    Returns a simple JSON response
    """
    return {"message": "Hello World!"}
