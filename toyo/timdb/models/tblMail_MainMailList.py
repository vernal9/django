from django.db import models,connection
from django.contrib import admin
from datetime import date
from django.utils import timezone
# Create your models here.

GROUP_CHOICES = [
    ('財會相關部門','財會相關部門'),
    ('收件者未知','收件者未知'),
    ('行政資訊職安','行政資訊職安'),
    ('總經理室', '總經理室'),

]

class NOGetMAILManager(models.Manager):
    def get_query_set(self):
        return super(NOGetMAILManager, self).get_query_set().filter(MAILTakeDate__isnull=True)


class tblMAIL_MainMailList(models.Model):

    id = models.CharField(verbose_name='id',max_length=5,primary_key=True,db_column='MAILKEY')
    MAILInDate = models.DateTimeField(verbose_name="刷入日期",db_column='MAILInDate')
    MAILSN = models.IntegerField(db_column='MAILSN')
    MAILEditDate = models.DateTimeField(verbose_name="編輯日期",db_column='MAILEditDate')
    MAILFrom = models.CharField(verbose_name='寄件單位',db_column='MAILFrom',max_length=20)
    MAILTo = models.CharField(verbose_name='收件人',db_column='MAILTo',max_length=20)
    MAILGroup = models.CharField(verbose_name='收件群組',db_column='MAILGroup',max_length=20,choices=GROUP_CHOICES)
    MAILMemo = models.TextField(verbose_name='備註',db_column='MAILMemo')
    MAILTakeDate = models.DateTimeField(verbose_name="取件日期",db_column='MAILTakeDate')
    MAILTakeWN = models.CharField(verbose_name='取件人工號',db_column='MAILTakeWN',max_length=10)
    MAILTakeName = models.CharField(verbose_name='取件人姓名',db_column='MAILTakeName',max_length=10)
    MAILTakeMemo = models.TextField(verbose_name='取件備註',db_column='MAILTakeMemo')
    MAILFlag = models.IntegerField(db_column='MAILFlag')
    objects = NOGetMAILManager()

    class Meta:
        app_label = 'timdb'
        verbose_name = '郵件登錄'
        db_table = 'tblMAIL_MainMailList'
        ordering = ['-id',]

    def __str__(self):
        return chr(self.MAILSN)

    def get_absolute_url(self):
        return reverse('timdb:list', args=[self.MAILSN])

    def get_mail_group():
        return



@admin.register(tblMAIL_MainMailList)
class MainMailListAdmin(admin.ModelAdmin):

   list_display = ['MAILSN','MAILFrom','MAILTo','MAILGroup',]
   readonly_fields = ['id','MAILInDate','MAILSN',]
   search_fields = ['MAILGroup',]
   #設置可編輯字段
   #list_editable= ['MAILFrom','MAILTo','MAILGroup','MAILMemo',]
   #過濾選項
   #list_filter = ['',]
   #autocomplete_fields = ['',]
   list_per_page = 10


   #搜尋
   search_fields = ('MAILTo',)
   #日期月份篩選
   date_hierarchy = 'MAILInDate'
   #排序
   ordering = ('-MAILInDate',)


