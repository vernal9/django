"""ithome URL Configuration

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
from django.contrib import admin
from django.urls import path,include

from . import views
from .views import (VendorListView,VendorDetail,VendorCreateView,VendorUpdateView)
app_name = 'vendors'

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')), # 新增
    #path('', views.vendor_index, name="index"),
    #path('<int:id>/', views.singleVendor, name='vendor'),
    #path('create', views.vendor_create_view, name='create'),
    #path('test<int:id>/', views.singleVendor, name='vendor_id'),
    #path('fcreate', views.food_create_view, ),
    path('', VendorListView.as_view(), name='index'),
    path('<int:pk>/', VendorDetail.as_view(), name='vendor_id'),
    path('create/', VendorCreateView.as_view(), name='create'),
    path('<int:pk>/update/', VendorUpdateView.as_view(), name='update'),
]
