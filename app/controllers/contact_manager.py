from app.models.contact import Contact


class ContactManager:

    contacts_list = []

    def create_contact(self, new_contact: Contact):
        self.contacts_list.append(new_contact)

    def get_all_contacts(self):
        return self.contacts_list
