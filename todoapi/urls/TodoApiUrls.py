from django.urls import path
from todoapi.views import TodoListApiView
from todoapi.views import TodoDetailApiView

urlpatterns = [
    path('api', TodoListApiView.as_view()),
    path("api/<int:todo_id>", TodoDetailApiView.as_view()),
]