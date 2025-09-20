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
        assert list_to_test[i].contact_id == dummy_list[i].contact_id
        assert list_to_test[i].first_name == dummy_list[i].first_name
        assert list_to_test[i].last_name == dummy_list[i].last_name
        assert list_to_test[i].email == dummy_list[i].email
        assert list_to_test[i].phone == dummy_list[i].phone
        assert list_to_test[i].company == dummy_list[i].company
        assert list_to_test[i].industry == dummy_list[i].industry
        assert list_to_test[i].notes == dummy_list[i].notes


def test_create_contact(dummy_list: List[Contact]):
    manager = ContactManager()
    manager.create_contact(dummy_list[0])
    assert len(manager.contacts_list) == 1
    assert manager.contacts_list[0].contact_id
    assert manager.contacts_list[0].first_name == "John"
    assert manager.contacts_list[0].last_name == "Doe"
    assert manager.contacts_list[0].email == "dummy@example.com"


def test_get_contact_by_id(dummy_list: List[Contact], id_to_find: str):
    manager = ContactManager()
    manager.contacts_list = dummy_list
