from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    salary = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.name} ({self.role})"
