from django.contrib import admin
from django.http import JsonResponse
from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


def home(request):
    return JsonResponse({
        "project": "NEXG HRMS",
        "version": "1.0",
        "status": "Running"
    })

urlpatterns = [
    path("", home),
    path("admin/", admin.site.urls),

    # Authentication
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    # HRMS Modules
    path("api/employees/", include("employees.urls")),
    path("api/departments/", include("departments.urls")),
    path("api/designations/", include("designations.urls")),
    path("admin/", admin.site.urls),
    path("api/employees/", include("employees.urls")),

]
