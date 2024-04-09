from django.db import models
from django.db import connection
from django.urls import reverse
from datetime import date
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib import admin
from rec.models import Recruit_Request,ServerValue

class Recruit_CheckList(models.Model):

    ID = models.IntegerField(primary_key=True,db_column='ID',default = 1)
    RequestID = models.ForeignKey(to='Recruit_Request',db_column='RequestID',on_delete=models.DO_NOTHING)
    CheckID = models.ForeignKey(to='ServerValue',db_column='CheckID',on_delete=models.DO_NOTHING)
    checked = models.BooleanField(db_column='checked',default=True)


    class Meta:
        verbose_name = '報到人員對應待辦狀態'
        app_label = 'rec'
        db_table = 'Recruit_CheckList'


    def __str__(self):
        if self.ID:
            return str(self.ID) + ' ' + str(self.RequestID)
        else: ' '

    def get_absolute_url(self):
        return reverse('rec:list', args=[self.ID])



@admin.register(Recruit_CheckList)
class Recruit_CheckListAdmin(admin.ModelAdmin):
   #list_display 是固定寫法,不可改寫
   #list_display=[field.name for field in Recruit_CheckList._meta.fields]
   feilds = ['ID','RequestID','CheckID','checked',]
   #過濾選項
   #list_filter = ('StringValue2',)
   #搜尋
   #search_fields = ('StringValue1',)
   #排序
   #ordering = ('StringValue2',)






