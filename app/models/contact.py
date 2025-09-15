from pydantic import BaseModel
from typing import Optional
from typing import List
import uuid


class Contact(BaseModel):
    contact_id: uuid.UUID
    first_name: str
    last_name: str
    email: str
    phone: Optional[str] = None
    company: Optional[str] = None
    industry: Optional[str] = None
    notes: Optional[List[str]] = None
