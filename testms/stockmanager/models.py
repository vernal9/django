from django.db import models
from django.urls import reverse
# Create your models here.

class closestoack(models.Model):
    closecategory=[
        ('TY制服_長黑', "TY制服_長黑"),
        ('TY制服_短黑', "TY制服_短黑"),
        ('TY制服_短白', "TY制服_短白"),
    ]

    closesize = [
        ('S', "S"),
        ('M', "M"),
        ('L', "L"),
        ('XL', "XL"),
        ('2XL', "2XL"),
        ('3XL', "3XL"),
        ('4XL', "4XL"),
        ('5XL', "5XL"),
    ]

    close_sn = models.AutoField(primary_key=True,db_column='close_sn')
    close_id = models.CharField(verbose_name="制服類型",db_column='close_id',max_length=50,choices=closecategory)
    close_size = models.CharField(verbose_name="制服尺寸", db_column='close_size',max_length=5,choices=closesize)
    close_number = models.IntegerField(verbose_name="數量",db_column='close_number',)
    close_employee = models.CharField(verbose_name="登錄員工", db_column='close_employee',max_length=10)


    class Meta:
        verbose_name = "制服庫存管理"
        db_table = "close_stock"

    def __str__(self):
        return self.close_id

    def get_absolute_url(self):
        return reverse('stockmanager:closestock_create', kwargs={'pk':self.pk})