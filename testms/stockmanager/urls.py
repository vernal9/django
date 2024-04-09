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

app_name = 'stockmanager'

urlpatterns = [
    #create a task
    path('create/',views.ClosestockCreateView.as_view(),name='closestock_create'),
    path('update/<int:pk>/', views.ClosestockUpdate.as_view(), name='closestock_update'),
    path('del/<int:pk>/', views.ClosestockDelete.as_view(), name='closestock_del'),

    #review task list
    path('', views.ClosestockListView.as_view(),name='closestock_list'),
    path('list', views.ClosestockListView.as_view(),name='closestock_list'),



]
