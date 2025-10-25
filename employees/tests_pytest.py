import pytest
from rest_framework.test import APIClient
from .models import Employee

@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def employee(db):
    return Employee.objects.create(name="John", role="Lead", salary="80000.00")

@pytest.mark.django_db
def test_create_employee(client):
    response = client.post("/employees/", {
        "name": "Alice",
        "role": "Developer",
        "salary": "75000.00"
    }, format="json")
    assert response.status_code == 201
    assert response.data["name"] == "Alice"

@pytest.mark.django_db
def test_get_employee_list(client, employee):
    response = client.get("/employees/")
    assert response.status_code == 200
    assert len(response.data) == 1

@pytest.mark.django_db
def test_get_employee_by_id(client, employee):
    response = client.get(f"/employees/{employee.id}/")
    assert response.status_code == 200
    assert response.data["name"] == "John"
    assert response.data["role"] == "Lead"

@pytest.mark.django_db
def test_update_employee(client, employee):
    response = client.put(f"/employees/{employee.id}/", {
        "name": "John",
        "role": "Senior Lead",
        "salary": "90000.00"
    }, format="json")
    assert response.status_code == 200
    assert response.data["role"] == "Senior Lead"

@pytest.mark.django_db
def test_delete_employee(client, employee):
    response = client.delete(f"/employees/{employee.id}/")
    assert response.status_code == 204
