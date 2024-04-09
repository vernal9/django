from django.db import models
from django.db.models import Q
from django.contrib import admin
from django.db import connection
from django.utils.translation import gettext_lazy as _
import datetime


# Create your models here.

class fom13(models.Model):

    category = [
        ('PGR','程式異動'),
        ('DATA','資料處理'),
    ]

    FORM_NO = models.CharField(max_length=10,primary_key=True,db_column='FORM_NO')
    APPLY_DATE = models.DateTimeField(db_column='APPLY_DATE',verbose_name='申請日期')
    APPLY_EMP_NO = models.CharField(max_length=6,db_column='APPLY_EMP_NO',verbose_name='申請人工號')
    APPLY_EMP_NAME = models.CharField(max_length=6, db_column='APPLY_EMP_NAME',verbose_name='申請人姓名')
    APPLY_NOTE = models.TextField(db_column='APPLY_NOTE',verbose_name='需求說明')
    SYS_OWNER = models.CharField(max_length=6, db_column='SYS_OWNER',verbose_name='處理人員')
    CLOSEDATE = models.DateTimeField(max_length=10,db_column='CLOSED_DATE', verbose_name='結案日期',blank=True)
    APPSTATUS = models.CharField(max_length=10, db_column='APP_STATUS', verbose_name='狀態')
    SYS_PGR = models.CharField(max_length=10, db_column='SYS_PGR', verbose_name='程式代號',blank=True)
    SYS_REQ = models.CharField(max_length=10,db_column='SYS_REQ',verbose_name='類別',choices=category)

    class Meta:
        verbose_name = 'FM013'
        app_label = 'form'
        db_table = '[form].[dbo].[FM013_HEADER]'
        ordering = ['APPLY_DATE',]


    def __str__(self):
        return self.APPSTATUS+' '+self.APPLY_EMP_NO

#自定義查詢
class overdueFilter(admin.SimpleListFilter):
    title = _('結案否')
    parameter_name = 'APPSTATUS'
    default_value = '進行中'

    def lookups(self, request, model_admin):
        return (
            ('進行中', _('進行中')),
            ('已結案',_('已結案')),
        )

    def queryset(self, request, queryset):
        if self.value() == '進行中':
            return queryset.filter(Q(CLOSEDATE__isnull=True,APPSTATUS='WA'))
        if self.value() == '已結案':
            return queryset.filter(Q(CLOSEDATE__isnull=False))


    """預設篩選值"""
    def value(self):
        value = super(overdueFilter,self).value()
        if value is None:
            value = self.default_value
        else:
            self.default_value = value
        return str(value)


@admin.register(fom13)
class fom13Admin(admin.ModelAdmin):
    # list_display 是固定寫法,不可改寫
    #list_display = [field.name for field in fom13._meta.fields]
    list_display = ('FORM_NO','APPLY_EMP_NAME','APPLY_EMP_NO','APPLY_NOTE','SYS_PGR',)
    exclude = ['FORM_NO',]
    # 過濾選項
    list_filter = (overdueFilter,)
    # 搜尋
    search_fields = ('SYS_OWNER','FORM_NO','APPLY_EMP_NAME')
    #ordering = ('date_adenddate',)

    def get_queryset(self, request):
        qs = super(fom13Admin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs.filter(SYS_OWNER='T18026')
        else:
            return qs.filter(SYS_OWNER=request.user)

