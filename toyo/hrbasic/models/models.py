from django.db import models
from django.contrib import admin

# Create your models here.
class Dep(models.Model):

    code = models.CharField(max_length=10,primary_key=True,db_column='code')
    name = models.CharField(max_length=20,db_column='name')

    class Meta:
        app_label = 'hrbasic'
        db_table = 'Department'
        ordering = ['code',]
        verbose_name = '部門'


    def __str__(self):
        return "hrbasic %s" % self.code+' '+self.name or ' '

    def get_absolute_url(self):
        return reverse('hrbasic:list', args=[self.code])

@admin.register(Dep)
class DepAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Dep._meta.fields]
    search_fields = ['code','name',]

class Emp(models.Model):

    code = models.CharField(max_length=10,primary_key=True,db_column="code")
    cnname = models.CharField(max_length=20,db_column="cnname")

    class Meta:
        app_label = 'hrbasic'
        db_table = 'Employee'
        ordering = ['code',]


    def __str__(self):
        return self.code+' '+self.cnname

    def get_absolute_url(self):
        return reverse('hrbasic:list', args=[self.code])



