from django.db import models,connection
from django.contrib import admin



# Create your models here.
class OrganizationUnit(models.Model):

    id = models.CharField(verbose_name='id',max_length=10,primary_key=True)
    organizationUnitName = models.CharField(max_length=20)

    class Meta:
        app_label = 'bpm'
        db_table = 'OrganizationUnit'
        ordering = ['id',]

    def __str__(self):
        return self.id+ ' ' +self.organizationUnitName

    def get_absolute_url(self):
        return reverse('bpm:list', args=[self.organizationUnitName])

class TYHR11Manager(models.Manager):
    def get_queryset(self):
        return super(TYHR11Manager, self).get_queryset().filter(drp_status='W')

class TYHR11(models.Model):
    drpstatus = [('W','待報到'),
                 ('Y','已報到'),
                 ('X','取消報到'),
                 ]

    formSerialNumber = models.CharField(primary_key=True,max_length=40)
    txt_code = models.CharField(verbose_name="預取工號",max_length=6,db_column='txt_code')
    txt_name = models.CharField(verbose_name="姓名",max_length=20)
    dia_dep = models.ForeignKey(on_delete=models.CASCADE,verbose_name="預計部門",db_column='dia_dep', to='OrganizationUnit',
                               )
    drp_status = models.CharField(verbose_name="人員狀態",max_length=1,choices=drpstatus,default='W')
    txt_note = models.TextField(verbose_name="備註",blank=True)
    date_date = models.DateField(verbose_name="預計報到日")
    objects = TYHR11Manager()

    class Meta:
        verbose_name = '預取工號'
        app_label = 'bpm'
        db_table = "TYHR11"

    def __str__(self):
        return self.txt_name

    def get_absolute_url(self):
        return reverse('bpm:list', args=[self.txt_name])




@admin.register(TYHR11)
class TYHR11Admin(admin.ModelAdmin):
    # list_display 是固定寫法,不可改寫
    list_display = [field.name for field in TYHR11._meta.fields]
    # 過濾選項
    list_filter = ('drp_status',)
    # 搜尋
    search_fields = ('txt_name',)
    # list_display = ['id', 'vendor_name', 'store_name', 'phone_number', 'address']
    # 日期月份篩選
    #date_hierarchy = 'date_date'
    # 排序
    ordering = ('date_date',)
    #唯讀
    #readonly_fields = ('OID',)

    #def formfield_for_foreignkey(self, db_field, request, **kwargs):
    #    if db_field.name=="dia_dep":
    #        kwargs["queryset"] = OrganizationUnit.objects.filter(id__contains = 'T')
    #    return super().formfield_for_foreignkey(db_field, request, **kwargs)







