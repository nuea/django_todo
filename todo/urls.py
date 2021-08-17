from django.urls import path
from todo import views

urlpatterns = [
    path("create/", views.CreateTodoAPIView.as_view(),name="create_todo"),
    path("all/", views.ListTodoAPIView.as_view(),name="list_todo"),
    path("update/<int:pk>/",views.UpdateTodoAPIView.as_view(),name="update_todo"),
    path("delete/<int:pk>/",views.DeleteTodoAPIView.as_view(),name="delete_todo")
]