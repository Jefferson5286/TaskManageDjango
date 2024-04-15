from django.contrib import admin
from django.urls import path
from rest_framework import permissions

from tasks.views import create_task, create_many_tasks, delete_many_tasks
from tasks.api.generics import *


urlpatterns = [
    path('admin', admin.site.urls),

    path('create-task', create_task, name='create-task'),
    path('update-task/<str:pk>', TaskUpdate.as_view(), name='update-task'),
    path('delete-task/<str:pk>', TaskDelete.as_view(), name='delete-task'),
    path('task-list', TaskList.as_view(), name='task-list'),
    path('create-many-tasks', create_many_tasks, name='create-many-tasks'),
    path('delete-many-tasks', delete_many_tasks, name='delete-many-tasks'),
    path('task/<str:pk>', TaskDetail.as_view(), name='task-detail')
]
