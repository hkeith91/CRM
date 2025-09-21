from typing import List
from app.models.contact import Contact
from app.controllers.contact_manager import ContactManager
import uuid
import pytest


# TODO: Add test for valid phone number and email
# TODO: Add tests to test input validation
# TODO: Refactor tests to use __eq__


@pytest.fixture
def dummy_list():
    return [
        Contact(
            contact_id=str(uuid.uuid4()),
            first_name="John",
            last_name="Doe",
            email="dummy@example.com",
        ),
        Contact(
            contact_id=str(uuid.uuid4()),
            first_name="Jane",
            last_name="Smith",
            email="fake@notreal.com",
            phone="1234567890",
            company="Trucking Inc.",
            industry="Shipping",
            notes=["Contact early afternoons", "birthday in March"],
        ),
        Contact(
            contact_id=str(uuid.uuid4()),
            first_name="Adam",
            last_name="West",
            email="batman@justice.com",
            phone=None,
            company="Wayne Enterprises",
        ),
    ]


def test_contacts_list_initializes_to_empty():
    manager = ContactManager()

    assert len(manager.contacts_list) == 0


def test_get_all_contacts(dummy_list: List[Contact]):
    manager = ContactManager()
    list_to_test = manager.contacts_list = dummy_list

    assert len(manager.get_all_contacts()) == len(dummy_list)

    for i in range(len(dummy_list)):
        assert list_to_test[i] == dummy_list[i]


def test_create_contact(dummy_list: List[Contact]):
    manager = ContactManager()
    manager.create_contact(dummy_list[0])
    assert len(manager.contacts_list) == 1
    assert manager.contacts_list[0].contact_id
    assert manager.contacts_list[0].first_name == "John"
    assert manager.contacts_list[0].last_name == "Doe"
    assert manager.contacts_list[0].email == "dummy@example.com"


def test_get_contact_by_id_returns_correct_contact(dummy_list: List[Contact]):
    manager = ContactManager()
    manager.contacts_list = dummy_list

    contact_to_find = dummy_list[0]
    contact_id = contact_to_find.contact_id

    found_contact = manager.get_contact_by_id(contact_id)

    assert len(found_contact.__dict__) == len(contact_to_find.__dict__)
    assert found_contact == contact_to_find
