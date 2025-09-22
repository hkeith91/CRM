from typing import List
from app.models.contact import Contact, UpdateContact
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


@pytest.fixture
def dummy_update():
    return UpdateContact(
        first_name="Jonathan",
        last_name=None,
        email=None,
        company="Updated Company",
        industry="Updated Industry",
        notes=None,
    )


def test_contacts_list_initializes_to_empty():
    manager = ContactManager()

    assert len(manager.contacts_list) == 0


def test_get_all_contacts(dummy_list: List[Contact]):
    manager = ContactManager()
    manager.contacts_list = dummy_list

    assert len(manager.get_all_contacts()) == len(dummy_list)
    assert manager.get_all_contacts() == dummy_list


def test_create_contact(dummy_list: List[Contact]):
    manager = ContactManager()
    manager.create_contact(dummy_list[0])

    assert len(manager.contacts_list) == 1
    assert manager.contacts_list[0] == dummy_list[0]


def test_get_contact_by_id_returns_correct_contact(dummy_list: List[Contact]):
    manager = ContactManager()
    manager.contacts_list = dummy_list

    contact_to_find = dummy_list[0]
    contact_id = contact_to_find.contact_id

    found_contact = manager.get_contact_by_id(contact_id)

    assert len(found_contact.__dict__) == len(contact_to_find.__dict__)
    assert found_contact == contact_to_find


def test_get_contact_by_id_returns_none_if_not_found(dummy_list: List[Contact]):
    manager = ContactManager()
    manager.contacts_list = dummy_list

    non_existent_id = str(uuid.uuid4())

    found_contact = manager.get_contact_by_id(non_existent_id)

    assert found_contact == None


def test_update_contact_returns_true_on_success(
    dummy_list: List[Contact], dummy_update: UpdateContact
):
    manager = ContactManager()
    manager.contacts_list = dummy_list
    contact_to_update = manager.contacts_list[0]

    # Assert update_contact method returns True
    assert manager.update_contact(contact_to_update.contact_id, dummy_update) == True

    found_contact = manager.get_contact_by_id(contact_to_update.contact_id)
    assert found_contact == contact_to_update


@pytest.mark.parametrize(
    "email, expected_result",
    [
        ("test@example.com", True),
        ("john.doe123@sub.domain.co.uk", True),
        ("valid_email@test-server.net", True),
        ("invalid=email", False),
        ("no-at-sign.com", False),
        ("@missingusername.org", False),
        ("name@domain_with_underscore.com", False),
    ],
)
def test_check_valid_email(email, expected_result):
    contact = Contact(
        contact_id=str(uuid.uuid4()), first_name="Test", last_name="User", email=email
    )

    assert contact.check_valid_email() == expected_result
