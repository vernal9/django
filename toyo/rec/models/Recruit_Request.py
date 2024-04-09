from django.db import models
from django.db import connection
from django.urls import reverse
from datetime import date
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib import admin


import random
# Create your models here.

#人員來源
RT_CHOICES = [
    (0,'0:人力銀行'),
    (1,'徵才活動'),
    (2,'親友介紹'),
    (1000, '其他'),
]

def random_int():
    return int(random.randrange(10000,99999))

class Recruit_Request(models.Model):
    # 狀態碼
    STATUE = [
        (1, '無法聯絡上本人'),
        (2, '答應參加面試'),
        (3, '考慮中'),
        (4, '婉拒'),
        (8, '未依約面試'),
        (9, '取消面試'),
        (10, '未錄取 '),
        (12, '基本資料卡填寫完成'),
        (13, '完成報到資料填寫'),
        (14, '完成任用單'),
    ]

    ID = models.BigAutoField(primary_key=True,db_column='ID')
    VerificationCode = models.IntegerField(verbose_name="驗證碼",default=random_int)
    RequestDep = models.ForeignKey(verbose_name="需求部門",to='hrbasic.Dep',
                                   on_delete=models.DO_NOTHING,db_column='RequestDep',
                                   db_constraint=False)
    RequestTime = models.DateField(verbose_name="接收日期",default=date.today)
    RecruitRequestType = models.IntegerField(verbose_name="來源類型",
                                             choices=RT_CHOICES,default=0)
    RecruitRequestComment = models.CharField(verbose_name="履歷編號",max_length=255,blank=True)
    CandidatesName = models.CharField(verbose_name="面試人姓名",max_length=20)
    JobName = models.CharField(verbose_name="應徵職務",max_length=20)
    PhoneNumber = models.CharField(verbose_name="聯絡電話",max_length=15,blank=True)
    CandidatesMail = models.EmailField(verbose_name="Email",blank=True)
    Remarks = models.TextField(verbose_name="備註",max_length=255,blank=True)
    InterviewTime = models.DateTimeField(verbose_name="面試日期")
    RecruitStatus = models.IntegerField(verbose_name="狀態",choices=STATUE,default=2)
    IsFinished = models.IntegerField(verbose_name="結案否",choices=[(0,'未結案'),(1,'結案')])

    class Meta:
        verbose_name = '招募登錄'
        app_label = 'rec'
        db_table = "Recruit_Request"
        ordering = ['-RecruitStatus']

    def __str__(self):
        return str(self.ID) + ' ' +self.CandidatesName

    def get_absolute_url(self):
        return reverse('rec:list', args=[self.ID])



#增加自定義篩選
class Recruit_RequestFilter(admin.SimpleListFilter):
    title = _('結案否')
    parameter_name = 'IsFinished'
    default_value = '未結案'

    def lookups(self, request, model_admin):
        return (
            ('未結案',_('未結案')),
            ('已結案',_('已結案')),
        )

    def queryset(self, request, queryset):
        if self.value() == '未結案':
            return queryset.filter(IsFinished=0)
        if self.value() == '已結案':
            return queryset.filter(IsFinished=1)

    def value(self):
        value = super(Recruit_RequestFilter, self).value()
        if value is None:
            value = self.default_value
        else:
            self.default_value = value
        return str(value)


@admin.register(Recruit_Request)
class Recruit_RequestAdmin(admin.ModelAdmin):
   #list_display 是固定寫法,不可改寫
   #list_display = [field.name for field in RRequest._meta.fields]
   list_display = ['ID','CandidatesName','RecruitStatus','InterviewTime','IsFinished','Remarks',]
   #設置可編輯字段
   list_editable= ['IsFinished',]
   #過濾選項
   list_filter = ['RecruitStatus',Recruit_RequestFilter]
   autocomplete_fields = ['RequestDep',]
   list_per_page = 5

   #搜尋
   search_fields = ('CandidatesName','ID',)
   #list_display = ['id', 'vendor_name', 'store_name', 'phone_number', 'address']
   #日期月份篩選
   date_hierarchy = 'InterviewTime'
   #排序
   ordering = ('InterviewTime',)
   inlines = [
    #   CheckListInline,
   ]







