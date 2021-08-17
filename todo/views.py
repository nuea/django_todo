from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView
from .serializers import TodoSerializer
from .models import Todo

# Create your views here.
class CreateTodoAPIView(CreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class ListTodoAPIView(ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class UpdateTodoAPIView(UpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class DeleteTodoAPIView(DestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer