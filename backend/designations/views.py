from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Designation
from .serializers import DesignationSerializer

class DesignationViewSet(viewsets.ModelViewSet):
    queryset = Designation.objects.all().order_by("name")
    serializer_class = DesignationSerializer
    permission_classes = [AllowAny]
