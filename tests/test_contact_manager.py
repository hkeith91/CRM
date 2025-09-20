from typing import List
from app.models.contact import Contact
from app.controllers.contact_manager import ContactManager
import uuid
import pytest


# TODO: Add test for valid phone number and email
# TODO: Add tests to test input validation


@pytest.fixture
def dummy_list():
    return [
        Contact(
            contact_id=uuid.uuid4(),
            first_name="John",
            last_name="Doe",
            email="dummy@example.com",
        ),
        Contact(
            contact_id=uuid.uuid4(),
            first_name="Jane",
            last_name="Smith",
            email="fake@notreal.com",
            phone="1234567890",
            company="Trucking Inc.",
            industry="Shipping",
            notes=["Contact early afternoons", "birthday in March"],
        ),
        Contact(
            contact_id=uuid.uuid4(),
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
    manager.contacts_list = dummy_list

    assert len(manager.get_all_contacts()) == len(dummy_list)

    for i in range(len(dummy_list)):
        assert manager.get_all_contacts()[i].contact_id == dummy_list[i].contact_id
        assert manager.get_all_contacts()[i].first_name == dummy_list[i].first_name
        assert manager.get_all_contacts()[i].last_name == dummy_list[i].last_name
        assert manager.get_all_contacts()[i].email == dummy_list[i].email
        assert manager.get_all_contacts()[i].phone == dummy_list[i].phone
        assert manager.get_all_contacts()[i].company == dummy_list[i].company
        assert manager.get_all_contacts()[i].industry == dummy_list[i].industry
        assert manager.get_all_contacts()[i].notes == dummy_list[i].notes


def test_create_contact(dummy_list: List[Contact]):
    manager = ContactManager()
    manager.create_contact(dummy_list[0])
    assert len(manager.contacts_list) == 1
    assert manager.contacts_list[0].contact_id
    assert manager.contacts_list[0].first_name == "John"
    assert manager.contacts_list[0].last_name == "Doe"
    assert manager.contacts_list[0].email == "dummy@example.com"
