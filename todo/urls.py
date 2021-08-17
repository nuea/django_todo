from django.urls import path
from todo import views

urlpatterns = [
    path("create/", views.CreateTodoAPIView.as_view(),name="todo_create")
]