from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import uuid

app = FastAPI()


class Contact(BaseModel):
    name: str
    email: str
    phone: Optional[str] = None
    company: Optional[str] = None
