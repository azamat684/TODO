from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import TaskSerializer
from .models import Task
from .pagination import CustomPagination
from rest_framework.throttling import UserRateThrottle
class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    pagination_class = CustomPagination
    throttle_classes = [UserRateThrottle]
