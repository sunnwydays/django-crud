from .models import Record
import pytest
from django.test import TestCase
from django.urls import reverse

#testing the model
@pytest.fixture
def record():
    return Record.objects.create(
        first_name="John",
        last_name="Doe",
        email="john.doe@example.com",
        phone="12345678901",
        address="123 Main St",
        city="Anytown",
        province="Anystate",
        country="Country"
    )

def test_record_creation(record):
    assert isinstance(record, Record)
    assert record.first_name == "John"
    assert record.last_name == "Doe"
    assert record.email == "john.doe@example.com"
    assert record.phone == "12345678901"
    assert record.address == "123 Main St"
    assert record.city == "Anytown"
    assert record.province == "Anystate"
    assert record.country == "Country"

def test_record_str(record):
    expected_str = "John Doe"
    assert str(record) == expected_str


#testing update-record

def test_update_record_form_post(client, record):
    form_data = {
        "first_name": "John",
        "last_name": "Doe",
        "email": "john.doe@example.com",
        "phone": "12345678901",
        "address": "123 Main St",
        "city": "Anytown",
        "province": "Anystate",
        "country": "Country"
    }
    response = client.post(reverse('update-record', kwargs={'pk': record.id}), form_data)
    assert response.status_code == 302
    assert response.url == reverse("dashboard")
    updated_record = Record.objects.get(id=record.id)
    assert updated_record.first_name == 'John'
    assert updated_record.province == 'Anystate'
