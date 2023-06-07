from django.shortcuts import render
from rest_framework import viewsets
from .serializers import Taskserializers, Userserializers
from .models import Task
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView

# Create your views here.

class Taskviewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset=Task.objects.all().order_by('-date_created')
    serializer_class = Taskserializers
class DueTaskViewset(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-date_created').filter(completed=False)
    serializer_class = Taskserializers
class CreateusrView(CreateAPIView):
    model=get_user_model()
    permission_classes = (AllowAny,)
    serializer_class = Userserializers
class CompletedTaskViewset(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-date_created').filter(completed=True)
    serializer_class = Taskserializers