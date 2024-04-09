from django.db import models
from django.contrib import admin

# Create your models here.
class dep(models.Model):
    code = models.CharField(verbose_name="部門編號",max_length=20)
    name = models.CharField(verbose_name="部門名稱", max_length=20)
    class Meta:
        app_label = 'basic'
        db_table = 'department'


class clothing(models.Model):
    code = models.CharField(verbose_name="制服編號",max_length=20)
    name = models.CharField(verbose_name="制服名稱", max_length=20)
    class Meta:
        app_label = 'basic'
        db_table = 'clothing'
