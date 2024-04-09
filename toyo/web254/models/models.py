from django.db import models
from django.contrib import admin
from django.db import connection

# Create your models here.

class daily(models.Model):

    IDENTIFY = models.CharField(max_length=10,primary_key=True,db_column='IDENTIFY')
    WORK_DATE = models.CharField(max_length=10,db_column='WORK_DATE')
    CREATE_USER_ID = models.CharField(max_length=6,db_column='CREATE_USER_ID')
    MEMO = models.TextField(db_column='MEMO')


    class Meta:
        verbose_name = '個人日誌'
        app_label = 'web254'
        db_table = '[toyo_web].[dbo].[EMPLOYEE_DIARY_HEAD]'
        ordering = ['WORK_DATE',]


    def __str__(self):
        return self.WORK_DATE+' '+self.CREATE_USER_ID


   # def get_absolute_url(self):
   #     return reverse('hrbasic:list', args=[self.code])

@admin.register(daily)
class dailyAdmin(admin.ModelAdmin):
    # list_display 是固定寫法,不可改寫
    #list_display = [field.name for field in daily._meta.fields]
    # 過濾選項
    list_filter = ('CREATE_USER_ID','WORK_DATE',)

    # 搜尋
    search_fields = ('CREATE_USER_ID','WORK_DATE','MEMO',)
    list_display = ['IDENTIFY', 'WORK_DATE', 'CREATE_USER_ID','MEMO',]
    #list_editable = ['MEMO',]
    # 日期月份篩選
    #date_hierarchy = 'WORK_DATE'
    # 排序
    ordering = ('-WORK_DATE',)

    def get_queryset(self, request):
        qs = super(dailyAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs.filter(CREATE_USER_ID='T18026')
        else:
            return qs.filter(CREATE_USER_ID=request.user)

class req(models.Model):

    req_raise_no = models.CharField(max_length=10,primary_key=True,db_column='req_raise_no')
    req_raise_date = models.CharField(max_length=10,db_column='req_raise_date')
    req_close_userid = models.CharField(max_length=6,db_column='req_close_userid')
    req_content = models.TextField(db_column='req_content')
    req_close_observation = models.CharField(max_length=5,db_column='req_close_observation')

    class Meta:
        verbose_name = 'REQ'
        app_label = 'web254'
        db_table = '[toyo_web].[dbo].[Sign_Req]'
        ordering = ['req_raise_date',]

    def __str__(self):
        return self.req_raise_no

@admin.register(req)
class reqAdmin(admin.ModelAdmin):
    # list_display 是固定寫法,不可改寫
    list_display = [field.name for field in req._meta.fields]
    # 過濾選項
    list_filter = ('req_close_observation',)

    # 搜尋
    search_fields = ('req_close_userid','req_content',)
    #list_editable = ['MEMO',]
    # 日期月份篩選
    #date_hierarchy = 'WORK_DATE'
    # 排序
    ordering = ('-req_raise_date',)

    def get_queryset(self, request):
        qs = super(reqAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs.filter(req_close_userid='T18026',req_close_observation='Wait')
        else:
            return qs.filter(req_close_userid=request.user)






