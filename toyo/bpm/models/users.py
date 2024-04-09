from django.db import models,connection
from django.contrib import admin

class EmpManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(leaveDate__isnull=True)

class Emp(models.Model):
    id = models.CharField(verbose_name='工號',max_length=10,primary_key=True,db_column='id')
    userName = models.CharField(verbose_name='姓名',max_length=10,db_column='userName')
    leaveDate = models.DateField(verbose_name='離職日',db_column='leaveDate')
    objaect = EmpManager()

    class Meta:
        verbose_name = '員工資料'
        app_label = 'bpm'
        db_table = 'Users'
        ordering = ['id',]


    def __str__(self):
        #return str(self.id)+str(' ')+str(self.userName)
        return "%s" % self.id + ' ' + self.userName or ' '

    def get_absolute_url(self):
        return reverse('bpm:list', args=[self.id])


@admin.register(Emp)
class EmpAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Emp._meta.fields]
    search_fields = ['id','userName',]
