from django.urls import path
from todoapi.views.TodoListApiView import TodoListApiView

urlpatterns = [
    path('api', TodoListApiView.as_view())
]