from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import PayrollViewSet

router = DefaultRouter()
router.register("", PayrollViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
