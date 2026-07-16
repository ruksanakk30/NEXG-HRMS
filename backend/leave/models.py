from django.db import models
from employees.models import Employee


class Leave(models.Model):

    LEAVE_TYPES = [
        ("Casual", "Casual"),
        ("Sick", "Sick"),
        ("Earned", "Earned"),
        ("Maternity", "Maternity"),
        ("Paternity", "Paternity"),
    ]

    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Approved", "Approved"),
        ("Rejected", "Rejected"),
    ]

    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE
    )

    leave_type = models.CharField(
        max_length=20,
        choices=LEAVE_TYPES
    )

    from_date = models.DateField()
    to_date = models.DateField()

    reason = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Pending"
    )

    applied_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.employee.employee_id} - {self.leave_type}"
