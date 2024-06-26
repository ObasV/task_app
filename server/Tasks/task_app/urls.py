from django.urls import path, re_path
from . import views

app_name = 'task_app'  

urlpatterns = [
    path('', views.landing_page, name = 'landing_page'),
    path('task/list', views.task_list, name='task_list'),
    path('task/detail/<int:pk>', views.task_detail, name='task_detail'),
    path('task/create', views.task_create, name='task_create'),
    path('task/update/<int:pk>', views.task_update, name='task_update'),
    path('task/delete/<int:pk>', views.task_delete, name='task_delete'),
]
