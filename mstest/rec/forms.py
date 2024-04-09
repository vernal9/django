import datetime

from django import forms
from .models import RRequest,Depment
from django.utils.translation import gettext_lazy as _


#新增
class RequestCreateForm(forms.ModelForm):

    class Meta:
        model = RRequest
        exclude = ['VerificationCode']
        widget = {
            'CandidatesMail': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:50%;'}),
            'InterviewTime': forms.DateTimeInput(attrs={'class': 'form-control', 'style': 'width:50%;'})

        }


#結案更新
class RequestFinishUpdate(forms.ModelForm):
    class Meta:
        model = RRequest
        fields = ['CandidatesName','IsFinished']

class RRequestForm(forms.ModelForm):
    class Meta:
        model = RRequest
        #fields = '__all__'
        exclude = ['VerificationCode']
        widget = {
            'CandidatesMail': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:50%;'}),

        }

        # 新增 labels 對應
        labels = {
            'VerificationCode': _('驗證碼'),
            'RequestTime': _('接收日期'),
            'RequestDep': _('需求部門'),
            'RecruitRequestType': _('來源類型'),
            'RecruitRequestComment':_('來源備註'),
            'CandidatesName': _('面試人姓名'),
            'JobName': _('應徵職務'),
            'PhoneNumber': _('聯絡電話'),
            'CandidatesMail': _('Email'),
            'InterviewTime': _('面試日期'),
            'Remarks': _('備註'),
            'RecruitStatus': _('狀態'),
            'IsFinished':_('結案否'),
        }

