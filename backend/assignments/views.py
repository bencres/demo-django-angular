from rest_framework import viewsets
from .models import Assignment, Driver
from .serializers import AssignmentSerializer, DriverSerializer


class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    http_method_names = ['get', 'post', 'put', 'head', 'options']


class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    http_method_names = ['get', 'post', 'put', 'head', 'options']
