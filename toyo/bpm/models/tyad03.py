import datetime

from django.db import models,connection
from django.contrib import admin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from bpm.models import users


# Create your models here.

class TYAD03(models.Model):
    drpstatus = [('黑色-長袖制服','黑色-長袖制服'),
                 ('黑色-短袖制服','黑色-短袖制服'),
                 ('白色-短袖制服','白色-短袖制服'),
                 ]
    drpsize = [('S','S'),
               ('M','M'),
               ('L','L'),
               ('XL','XL'),
               ('2XL','2XL'),
               ('3XL','3XL'),
               ('4XL','4XL'),
               ('5XL','5XL'),
               ('其他','其他'),
    ]

    formSerialNumber = models.CharField(verbose_name='表單序號',primary_key=True,max_length=40)
    txt_sn = models.CharField(verbose_name='單號',  max_length=40)
    Dia_user = models.ForeignKey(verbose_name='申請人',to='Emp',db_column='Dia_user',on_delete=models.DO_NOTHING)
    drop_category = models.CharField(verbose_name="申請類別",max_length=10,choices=drpstatus)
    drop_size = models.CharField(verbose_name="更換規格", max_length=10, choices=drpsize)
    txt_num = models.IntegerField(verbose_name='更換數量',db_column='txt_num')
    text_applynote = models.TextField(verbose_name="更換原因",blank=True)
    date_get = models.DateField(verbose_name="領取日", db_column='date_get')
    txt_check = models.IntegerField(verbose_name='扣款數量',db_column='txt_check')
    text_adnote = models.TextField(verbose_name="行政備註", blank=True)
    txt_cost = models.IntegerField(verbose_name='扣款金額', db_column='txt_cost')
    txt_salarymonth = models.CharField(verbose_name='扣款薪資月', max_length=10)

    class Meta:
        verbose_name = '行政物品更換申請'
        app_label = 'bpm'
        db_table = "TYAD03"

    def __str__(self):
        return self.formSerialNumber

    def get_absolute_url(self):
        return reverse('bpm:list', args=[self.formSerialNumber])

#自定義查詢
class overdueFilter(admin.SimpleListFilter):
    title = _('查驗否')
    parameter_name = 'date_get'
    default_value = '未領取'

    def lookups(self, request, model_admin):
        return (
            ('未查驗', _('未查驗')),
            ('未領取',_('未領取')),
            ('需扣款', _('需扣款')),
        )

    def queryset(self, request, queryset):
        if self.value() == '未查驗':
            return queryset.filter(txt_check__isnull=True)
        if self.value() == '未領取':
            return queryset.filter(date_get__isnull=True)
        if self.value() == '需扣款':
            return queryset.filter(txt_check__gt=0)

    """預設篩選值"""
    def value(self):
        value = super(overdueFilter,self).value()
        if value is None:
            value = self.default_value
        else:
            self.default_value = value
        return str(value)

@admin.register(TYAD03)
class TYAD03Admin(admin.ModelAdmin):
    # list_display 是固定寫法,不可改寫
    #list_display = [field.name for field in TYAD02._meta.fields]
    list_display = ('txt_sn','Dia_user','drop_category','txt_num','date_get','txt_check',)
    exclude = ['formSerialNumber',]
    autocomplete_fields = ['Dia_user',]
    # 過濾選項
    list_filter = ('drop_category',overdueFilter,)
    # 搜尋
    list_select_related = ('Dia_user',)
    search_fields = ('Dia_user__id','Dia_user__userName',)
    ordering = ('date_get',)

    #排版調整
    fieldsets = (
        ('申請', {
            'fields':('Dia_user', 'drop_category',
                      ('drop_size','txt_num'),'text_applynote',
                      ),
        }),
        ('行政填寫',{
            'classes':('collapse',),
            'fields':(('txt_check','txt_cost','txt_salarymonth'),'text_adnote',
            )
        }),
    )
