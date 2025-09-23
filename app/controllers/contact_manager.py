from app.models.contact import Contact, UpdateContact


# TODO: delete contact
# TODO: Require email OR phone


class ContactManager:

    def __init__(self):
        self.contacts_list = []

    def create_contact(self, new_contact: Contact):
        """
        Adds a new contact to the managers in-memory list
        """
        self.contacts_list.append(new_contact)

    def get_all_contacts(self):
        """
        Returns a list of all contacts.
        """
        return self.contacts_list

    def get_contact_by_id(self, id_to_find: str):
        """
        Finds a contact by their unique ID.
        Returns the Contact object if found, otherwise returns none.
        """
        found_contact = next(
            (
                contact
                for contact in self.contacts_list
                if contact.contact_id == id_to_find
            ),
            None,
        )
        return found_contact

    def update_contact(self, contact_to_update_id: str, update_contact: UpdateContact):
        found_contact = self.get_contact_by_id(contact_to_update_id)

        if not found_contact:
            print("Contact not found!")
            return False
        else:
            updated_data = update_contact.model_dump(exclude_none=True)
            updated_data.pop("contact_id", None)
            for field, value in updated_data.items():
                setattr(found_contact, field, value)

            return True
