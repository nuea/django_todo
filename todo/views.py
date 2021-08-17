from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView
from .serializers import TodoSerializer
from .models import Todo

# Create your views here.
class CreateTodoAPIView(CreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class ListTodoAPIView(ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer