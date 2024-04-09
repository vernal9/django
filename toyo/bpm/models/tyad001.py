from django.db import models,connection
from django.contrib import admin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from bpm.models import users
from django.db.models import Q


class TYAD01Manager(models.Manager):
    def get_queryset(self):
        return super(TYAD01Manager,self).get_queryset().filter(~Q(formSerialNumber='TYAD00100000000'))

class TYAD01(models.Model):

    formSerialNumber = models.CharField(primary_key=True,max_length=40,db_column='formSerialNumber')
    dia_user = models.ForeignKey(verbose_name='申請人',to='Emp',db_column='dia_user',on_delete=models.CASCADE)
    dia_dep = models.ForeignKey(verbose_name="需求部門", to='hrbasic.Dep',
                                   on_delete=models.DO_NOTHING, db_column='dia_dep',
                                   db_constraint=False)
    date_done = models.DateField(verbose_name="設定完成日",db_column='date_done')
    object = TYAD01Manager()

    class Meta:
        verbose_name = '員工車輛入廠申請'
        app_label = 'bpm'
        db_table = "TYAD01"

    def __str__(self):
        return self.formSerialNumber

    def get_absolute_url(self):
        return reverse('bpm:list', args=[self.formSerialNumber])



class TYAD01_cgrid(models.Model):
    drpstatus = [('汽車', '汽車'),
                 ('機車', '機車'),
                 ('腳踏車', '腳踏車'),
                 ]
    OID = models.CharField(primary_key=True, max_length=30, db_column='OID')
    formSerialNumber = models.ForeignKey(db_column='formSerialNumber', to='TYAD01',
                                         on_delete=models.CASCADE)
    txt_etag = models.CharField(verbose_name="etag",max_length=20,db_column='txt_etag')
    txt_carnum = models.CharField(verbose_name="車牌號碼",max_length=20,db_column='txt_carnum')
    drop_category = models.CharField(verbose_name="申請狀態",max_length=20,db_column='drop_category')
    drop_car = models.CharField(verbose_name="車輛種類", max_length=20, db_column='drop_car',choices=drpstatus)

    class Meta:
        verbose_name = '車輛資訊明細'
        app_label = 'bpm'
        db_table = "TYAD01_cgrid"

class cridSetInline(admin.TabularInline):
    model = TYAD01_cgrid
    fields = ['txt_etag','txt_carnum','drop_car','drop_category']
    extra = 0

@admin.register(TYAD01)
class TYAD01Admin(admin.ModelAdmin):

    autocomplete_fields = ['dia_user', ]
    # 過濾選項
    list_filter = ('tyad01_cgrid__drop_category','tyad01_cgrid__drop_car')
    # 搜尋
    list_select_related = ('dia_user',)
    search_fields = ('dia_user__id','dia_user__userName','tyad01_cgrid__txt_carnum')
    # 日期月份篩選
    date_hierarchy = 'date_done'
    # 排序
    ordering = ('-date_done',)
    # list_display 是固定寫法,不可改寫
    list_display = ['formSerialNumber', 'dia_user', 'date_done',]
   

    #唯讀
    readonly_fields = ('formSerialNumber',)
    inlines = [
        cridSetInline,
    ]









