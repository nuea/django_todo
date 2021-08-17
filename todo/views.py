from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from .serializers import TodoSerializer
from .models import Todo

# Create your views here.
class CreateTodoAPIView(CreateAPIView):
    """This endpoint allows for creation of a todo"""
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer