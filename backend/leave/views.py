from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .models import Leave
from .serializers import LeaveSerializer


class LeaveViewSet(viewsets.ModelViewSet):
    queryset = Leave.objects.all()
    serializer_class = LeaveSerializer
    permission_classes = [AllowAny]
