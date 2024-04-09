import datetime

from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from datetime import date
from django.utils import timezone
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
import random


# Create your models here.

#人員來源
RT_CHOICES = [
    (0,'人力銀行'),
    (1,'徵才活動'),
    (2,'親友介紹'),
    (1000, '其他'),
]

def random_int():
    return int(random.randrange(1000,9999))

class RRequest(models.Model):
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

    ID = models.BigAutoField(primary_key=True)
    VerificationCode = models.IntegerField(verbose_name="驗證碼",default=random_int)
    RequestTime = models.DateField(verbose_name="接收日期",default=date.today)
    RecruitRequestType = models.IntegerField(verbose_name="來源類型",
                                             choices=RT_CHOICES,default=0,blank=True)
    RecruitRequestComment = models.CharField(verbose_name="履歷編號",max_length=255,blank=True)
    CandidatesName = models.CharField(verbose_name="面試人姓名",max_length=20,error_messages={"blank":"請輸入姓名"})
    JobName = models.CharField(verbose_name="應徵職務",max_length=50)
    PhoneNumber = models.CharField(verbose_name="聯絡電話",max_length=12)
    CandidatesMail = models.EmailField(verbose_name="Email")
    Remarks = models.TextField(verbose_name="備註",max_length=255)
    InterviewTime = models.DateTimeField(verbose_name="面試日期",default=timezone.now())
    RecruitStatus = models.IntegerField(verbose_name="狀態",choices=STATUE)
    IsFinished = models.IntegerField(verbose_name="結案否",choices=[(0,'未結案'),(1,'結案')],default=0)
    RequestDep = models.CharField(verbose_name="需求部門",max_length=5)
    #RequestDep = models.ManyToManyField(to="dep")


    class Meta:
        verbose_name = "面試人員登錄"
        db_table = "Recruit_Request"
        ordering = ['-RecruitStatus']

    def __str__(self):
        return self.CandidatesName

    def get_absolute_url(self):
        return reverse('rec:list', args=[self.ID])

@admin.register(RRequest)
class RRequestAdmin(admin.ModelAdmin):
	#list_display 是固定寫法,不可改寫
	list_display = [field.name for field in RRequest._meta.fields]
	#list_display = ['id', 'vendor_name', 'store_name', 'phone_number', 'address']



class Extension(models.Model):
    code = models.CharField(max_length=10,db_column='code',primary_key=True)
    num = models.CharField(max_length=10)

    class Meta:
        db_table = "Extension"

    def __str__(self):
        return self.code

