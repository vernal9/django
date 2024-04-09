"""toyo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
#from django.contrib import admin
from django.urls import path,re_path
from . import views

app_name = 'rec'

urlpatterns = [

    path('',views.index,name='index'),
    path('list/',views.RequestListView.as_view(),name='rec-list'),
    path('add/',views.RequestCreateView.as_view(),name = 'rec-create'),
    path('<int:pk>/update/', views.RequestUpdateView.as_view(), name='rec-update'),
    path('<int:pk>/del/', views.RequestDeleteView.as_view(), name='rec-del'),
    path('extlist/',views.ExtensionView.as_view(),name = 'ext-list'),
    path('addext/', views.ExtAddView.as_view(), name = 'add_ext'),

]
