from django.db import models
from employees.models import Employee


class Payroll(models.Model):

    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Paid", "Paid"),
    ]

    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE
    )

    month = models.CharField(max_length=20)
    year = models.IntegerField()

    basic_salary = models.DecimalField(max_digits=10, decimal_places=2)

    overtime = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    bonus = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    deductions = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    net_salary = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    payment_date = models.DateField(
        null=True,
        blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Pending"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.employee.employee_id} - {self.month} {self.year}"
