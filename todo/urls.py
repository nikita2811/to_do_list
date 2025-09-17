from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'), 
    path("create", views.create, name='create'), 
    path("task/<int:task_id>", views.task_detail, name='task_detail'),
    path("delete/<int:task_id>", views.delete_task, name='delete'),
    path("edit/<int:task_id>", views.edit_task, name='edit'), 
    path("update/<int:task_id>", views.update_task, name='update'),  
]

