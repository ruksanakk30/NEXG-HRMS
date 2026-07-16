from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .models import Employee
from .serializers import EmployeeSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all().order_by("employee_id")
    serializer_class = EmployeeSerializer
    permission_classes = [AllowAny]

    # Search
    search_fields = [
        "employee_id",
        "first_name",
        "last_name",
        "email",
        "mobile",
    ]

    # Filter
    filterset_fields = [
        "department",
        "designation",
        "role",
        "is_active",
    ]

    # Sorting
    ordering_fields = [
        "employee_id",
        "joining_date",
        "salary",
        "created_at",
    ]

    # Default ordering
    ordering = ["employee_id"]
