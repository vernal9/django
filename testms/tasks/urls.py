"""testms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path,include,re_path
from . import views

app_name = 'tasks'

urlpatterns = [
    #create a task
    path('create/',views.task_create,name='task_create'),

    #review task list
    path('', views.task_list,name='task_list'),

    #retrieve single task object
    re_path(r'^(?P<pk>\d+)/$', views.task_detail, name='task_detail'),

     # Update a task
     re_path(r'^(?P<pk>\d+)/update/$', views.task_update, name='task_update'),


     # Delete a task
     re_path(r'^(?P<pk>\d+)/delete/$', views.task_delete, name='task_delete'),

]
