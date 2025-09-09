from pydantic import BaseModel
from typing import Optional
import uuid


class Contact(BaseModel):
    contact_id = uuid.uuid4()
    first_name: str
    last_name: str
    email: str
    phone: Optional[str] = None
    company: Optional[str] = None
    industry: Optional[str] = None
    notes: Optional[str] = None
