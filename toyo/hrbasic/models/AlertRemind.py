from django.db import models
from django.contrib import admin


class AlertRemind(models.Model):
    id = models.CharField(primary_key=True,db_column='RemindId',max_length=100)
    ARName = models.CharField(max_length=100,db_column='Name',verbose_name='名稱')
    ARContent = models.CharField(max_length=100,db_column='AlertContent',verbose_name='內容')
    ARTime = models.CharField(max_length=100,db_column='Requests',verbose_name='發送時間')
    IsActive = models.BooleanField(db_column='IsActive',verbose_name='執行否')

    class Meta:
        app_label = 'hrbasic'
        db_table = 'AlertRemind'
        ordering = ['ARName',]
        verbose_name = 'Alert'

    def __str__(self):
        return self.ARName or ' '

    def get_absolute_url(self):
        return reverse('hrbasic:list', args=[self.id])

class AlertReport(models.Model):
    AReportid = models.CharField(primary_key=True,db_column='AlertReportId',max_length=50)
    ARportName = models.CharField(db_column='Name',max_length=50,)
    ARportContent = models.TextField(db_column='AlertContent')

    class Meta:
        app_label = 'hrbasic'
        db_table = 'AlertReport'
        verbose_name = 'Alert 郵件設定'

    def __str__(self):
        return self.ARportName  or ' '

@admin.register(AlertReport)
class AlertReportAdmin(admin.ModelAdmin):
    list_display = [field.name for field in AlertReport._meta.fields]
    exclude = ['AReportid',]
    search_fields = ['ARportName','ARportContent',]
    ordering = ['ARportName',]

class AlertSet(models.Model):
    ASid = models.CharField(primary_key=True,db_column='AlertSetId',max_length=50)
    ADRid = models.ForeignKey(to='hrbasic.AlertRemind',db_column='RemindId',on_delete=models.DO_NOTHING)
    ASsql = models.TextField(db_column='SourceSql',verbose_name='SQL')
    ASRepportid = models.ForeignKey(to='AlertReport',db_column='AlertReportId',on_delete=models.DO_NOTHING)

    class Meta:
        app_label = 'hrbasic'
        db_table = 'AlertSet'
        verbose_name = 'Alert Sql'

class AlertSetInline(admin.StackedInline):
    model = AlertSet
    fields = ['ASsql','ASRepportid',]
    #欄位數量
    extra = 0

@admin.register(AlertRemind)
class AlertRemindAdmin(admin.ModelAdmin):
    #list_display = [field.name for field in AlertRemind._meta.fields]
    list_display = ['ARName','ARContent','ARTime',]
    exclude = ['id','ARTime',]
    search_fields = ['ARName','id',]
    list_filter =  ['IsActive',]
    ordering = ['-IsActive',]
    inlines = [
        AlertSetInline,
    ]


