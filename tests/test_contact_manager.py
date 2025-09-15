from typing import List
from app.models.contact import Contact
from app.controllers.contact_manager import ContactManager
import uuid
import pytest


# TODO: Add test for valid phone number and email
@pytest.fixture
def empty_list():
    return []


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


def test_get_all_contacts(dummy_list: List[Contact]):
    pass


def test_create_contact(empty_list: List[Contact]):
    contacts_list = []
