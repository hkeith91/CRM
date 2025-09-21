from pydantic import BaseModel
from typing import Optional
from typing import List
from email_validator import validate_email, EmailNotValidError


# TODO: Add demographics
# TODO: Add purchase history
# TODO: Add case history
# TODO: Add status (customer, prospect, vendor, etc)
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
        """
        Checks for equality with other Contact objects.
        """
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

    def __hash__(self):
        """
        Returns a hash of the Contact object based on its unique ID.
        """
        return hash(self.contact_id)

    def check_valid_email(self):
        """
        Checks if the contact's email is valid using the email_validator library.
        Returns True if valid, False otherwise.
        """
        try:
            validate_email(self.email)
            return True
        except EmailNotValidError:
            return False
