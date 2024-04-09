from django.contrib.auth import get_user_model
import django_filters
from django.db import models
from django.db import connection
from django.urls import reverse
from datetime import date
from django.utils import timezone
import django_tables2 as tables

import random


# Create your models here.
User = get_user_model()

#人員來源
RT_CHOICES = [
    (0,'0:人力銀行'),
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
                                             choices=RT_CHOICES,default=0)
    RecruitRequestComment = models.CharField(verbose_name="履歷編號",max_length=255)
    CandidatesName = models.CharField(verbose_name="面試人姓名",max_length=20)
    JobName = models.CharField(verbose_name="應徵職務",max_length=50)
    PhoneNumber = models.CharField(verbose_name="聯絡電話",max_length=12)
    CandidatesMail = models.EmailField(verbose_name="Email")
    InterviewTime = models.DateTimeField(verbose_name="面試日期",default='9998/12/31')
    Remarks = models.TextField(verbose_name="備註",max_length=255)
    RecruitStatus = models.IntegerField(verbose_name="狀態",choices=STATUE)
    IsFinished = models.IntegerField(verbose_name="結案否",choices=[(0,'未結案'),(1,'結案')],default=0)
    RequestDep = models.CharField(verbose_name="需求部門",max_length=5)
    #RequestDep = models.ManyToManyField(to="Depment")


    class Meta:
        db_table = "Recruit_Request"
        ordering = ['-RecruitStatus']

    def __str__(self):
        return self.CandidatesName

    def get_absolute_url(self):
        return reverse('rec:list', args=[self.ID])

#待辦基本資料檔
class ServerValue(models.Model):
    # 待辦類別選單
    StringValue2_Choice = [
        ('G1', '報到繳交'),
        ('G2', '發放品項'),
        ('G3', '行政資訊待辦'),
    ]

    ID = models.BigAutoField(primary_key=True)
    ValueType = models.IntegerField(default=4)
    StringValue1 = models.CharField(verbose_name="待辦事項說明",max_length=255)
    StringValue2 = models.CharField(verbose_name="待辦類別",max_length=4,choices=StringValue2_Choice)
    StringValue3 = models.CharField(verbose_name="份數/必要否",max_length=10)
    DateTimeValue1 = models.DateTimeField
    IntValue1 = models.IntegerField

    class Meta:
        db_table = "ServerValue"


    def __str__(self):
        return self.StringValue1


    #def get_absolute_url(self):
    #    return reverse('rec:list', args=[self.ID])

class CheckList(models.Model):
    ID = models.BigAutoField(primary_key=True)
    #RequestID = models.ForeignKey(RRequest,on_delete=models.CASCADE)
    CheckID = models.ManyToManyField('ServerValue')
    Checked = models.IntegerField(verbose_name="完成否",choices=[(0,'未結案'),(1,'結案')],default=0)
    CheckedTime = models.DateField

    class Meta:
        db_table = "Recruit_CheckList"

    def __str__(self):
        return self.ID


class Depment(models.Model):
    code = models.CharField
   # name = models.CharField

    class Meta:
        db_table = "department"
        app_label = 'HR'

    def __str__(self):
        return self.name

class SimpleTable(tables.Table):
    class Meta:
        model = ServerValue



