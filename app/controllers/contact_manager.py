from app.models.contact import Contact


# TODO: Add __eq__ to test equality
# TODO: get contact by id
# TODO: update contact by id
# TODO: delete contact
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
