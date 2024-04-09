from django.db import models
from django.db import connection
from django.urls import reverse
from datetime import date
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib import admin

class ServerValue(models.Model):

    TC_CHOICES = [
        ('G1', '新進繳交'),
        ('G2', '發放品項'),
        ('G3', '行政待辦'),
    ]

    ID = models.BigAutoField(primary_key=True,db_column='ID')
    ValueType = models.IntegerField(default=4)
    StringValue1 = models.CharField(verbose_name='待辦說明',max_length=50)
    StringValue2 = models.CharField(verbose_name='待辦類別',max_length=5,choices=TC_CHOICES)
    StringValue3 = models.CharField(verbose_name='份數與必要非必要',max_length=50,blank=True)

    class Meta:
        verbose_name = '待辦事項基礎設定'
        app_label = 'rec'
        db_table = 'ServerValue'

    def __str__(self):
        return self.StringValue1 or ' '

    def get_absolute_url(self):
        return reverse('rec:list', args=[self.ID])



@admin.register(ServerValue)
class ServerValueAdmin(admin.ModelAdmin):
   #list_display 是固定寫法,不可改寫
   list_display = [field.name for field in ServerValue._meta.fields]
   #過濾選項
   list_filter = ('StringValue2',)
   #搜尋
   search_fields = ('StringValue1',)
   #排序
   ordering = ('StringValue2',)