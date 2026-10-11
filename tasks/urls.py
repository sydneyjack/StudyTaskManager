
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("tasks/add/", views.add_task, name="add_task"),
    path("tasks/<int:task_id>/", views.task_detail, name="task_detail"),
    path(
        "tasks/<int:task_id>/toggle/",
        views.toggle_task,
        name="toggle_task",
    ),
    path(
        "tasks/<int:task_id>/delete/",
        views.delete_task,
        name="delete_task",
    ),
]
