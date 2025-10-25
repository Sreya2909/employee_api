from django.test import TestCase
from rest_framework.test import APIClient
from .models import Employee

class EmployeeAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.emp = Employee.objects.create(name="John", role="Lead", salary="80000.00")

    def test_create_employee(self):
        response = self.client.post(
            "/employees/",
            {
                "name": "Alice",
                "role": "Developer",
                "salary": "75000.00"
            },
            format="json"
        )
        self.assertEqual(response.status_code, 201)
        # ensure returned resource has expected name
        self.assertEqual(response.data["name"], "Alice")

    def test_get_employee_list(self):
        response = self.client.get("/employees/")
        self.assertEqual(response.status_code, 200)
        # one employee exists (created in setUp)
        self.assertEqual(len(response.data), 1)

    def test_get_employee_by_id(self):
        response = self.client.get(f"/employees/{self.emp.id}/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["name"], "John")
        self.assertEqual(response.data["role"], "Lead")

    def test_update_employee(self):
        response = self.client.put(
            f"/employees/{self.emp.id}/",
            {
                "name": "John",
                "role": "Senior Lead",
                "salary": "90000.00"
            },
            format="json"
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["role"], "Senior Lead")

    def test_delete_employee(self):
        response = self.client.delete(f"/employees/{self.emp.id}/")
        self.assertEqual(response.status_code, 204)
        # confirm it's gone
        self.assertEqual(Employee.objects.filter(id=self.emp.id).count(), 0)
