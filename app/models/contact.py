from pydantic import BaseModel
from typing import Optional
from typing import List
import uuid


class Contact(BaseModel):
    contact_id: str
    first_name: str
    last_name: str
    email: str
    phone: Optional[str] = None
    company: Optional[str] = None
    industry: Optional[str] = None
    notes: Optional[List[str]] = None

    def __eq__(self, other):
        if not isinstance(other, Contact):
            return NotImplemented
        return (
            self.contact_id == other.contact_id
            and self.first_name == other.first_name
            and self.last_name == other.last_name
            and self.email == other.email
            and self.phone == other.phone
            and self.company == other.company
            and self.industry == other.industry
            and self.notes == other.notes
        )
