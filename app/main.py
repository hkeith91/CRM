from fastapi import FastAPI, status, HTTPException
from .models.contact import Contact
from typing import List
import uuid

app = FastAPI()


# A temporary db for testing
contact_db: List[Contact] = []


@app.post("/contacts", status_code=status.HTTP_201_CREATED)
async def create_contact(new_contact: Contact):
    contact_db.append(new_contact)
    return {"data": new_contact}


@app.get("/")
async def hello_world():
    """
    This function handles GET requests to the root URL.
    Returns a simple JSON response
    """
    return {"message": "Hello World!"}
