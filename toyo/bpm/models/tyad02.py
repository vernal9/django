import datetime

from django.db import models,connection
from django.contrib import admin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from bpm.models import users


# Create your models here.

class TYAD02(models.Model):
    drpstatus = [('素食便當','素食便當'),
                 ('非豬葷便當','非豬葷便當'),
                 ('取消申請','取消申請'),
                 ]

    formSerialNumber = models.CharField(verbose_name='表單序號',primary_key=True,max_length=40)
    Dia_user = models.ForeignKey(verbose_name='申請人',to='Emp',db_column='Dia_user',on_delete=models.DO_NOTHING)
    txt_notemployee = models.CharField(verbose_name='非員工用餐人',max_length=20,db_column='txt_notemployee', blank=True)
    drop_category = models.CharField(verbose_name="申請類別",max_length=10,choices=drpstatus,default='W')
    date_adbegin = models.DateField(verbose_name="生效日", db_column='date_adbegin')
    date_adenddate = models.DateField(verbose_name="截止日", db_column='date_adenddate')
    text_applynote = models.TextField(verbose_name="申請備註",blank=True)
    date_begin = models.DateField(verbose_name="希望生效日", db_column='date_begin')
    date_enddate = models.DateField(verbose_name="希望截止日", db_column='date_enddate')
    text_adnote = models.TextField(verbose_name="行政備註", blank=True)

    class Meta:
        verbose_name = '特殊餐申請'
        app_label = 'bpm'
        db_table = "TYAD02"

    def __str__(self):
        return self.formSerialNumber

    def get_absolute_url(self):
        return reverse('bpm:list', args=[self.formSerialNumber])

#自定義查詢
class overdueFilter(admin.SimpleListFilter):
    title = _('過期否')
    parameter_name = 'date_adenddate'
    default_value = '進行中'

    def lookups(self, request, model_admin):
        return (
            ('進行中', _('進行中')),
            ('已過期',_('已過期')),
            ('未到期', _('未到期')),
        )

    def queryset(self, request, queryset):
        if self.value() == '進行中':
            return queryset.filter(date_adbegin__lte=datetime.date.today(),date_adenddate__gte=datetime.date.today())
        if self.value() == '已過期':
            return queryset.filter(date_adenddate__lte=datetime.date.today())
        if self.value() == '未到期':
            return queryset.filter(date_adbegin__gt=datetime.date.today())

    """預設篩選值"""
    def value(self):
        value = super(overdueFilter,self).value()
        if value is None:
            value = self.default_value
        else:
            self.default_value = value
        return str(value)

@admin.register(TYAD02)
class TYAD02Admin(admin.ModelAdmin):
    # list_display 是固定寫法,不可改寫
    #list_display = [field.name for field in TYAD02._meta.fields]
    list_display = ('formSerialNumber','Dia_user','drop_category','txt_notemployee','date_adbegin','date_adenddate',)
    exclude = ['formSerialNumber',]
    autocomplete_fields = ['Dia_user',]
    # 過濾選項
    list_filter = ('drop_category',overdueFilter,)
    # 搜尋
    list_select_related = ('Dia_user',)
    search_fields = ('Dia_user__id','Dia_user__userName',)
    ordering = ('date_adenddate',)

    #排版調整
    fieldsets = (
        ('申請', {
            'fields':('Dia_user', 'txt_notemployee','drop_category',
                      ('date_begin','date_enddate'),'text_applynote',
                      ),
        }),
        ('行政填寫',{
            'classes':('collapse',),
            'fields':(('date_adbegin','date_adenddate'),'text_adnote',
            )
        }),
    )












