import calendar

from django import forms
from django.forms import widgets
from .models.Recruit_Request import Recruit_Request
from hrbasic.models import *

class RRequestForm(forms.ModelForm):

    class Meta:
        model = Recruit_Request
        localized_fields = "__all__"
        field = "__all__"
        exclude = ['VerificationCode',]
        InterviewTime = calendar.HTMLCalendar
        widgets = {
            'CandidatesName': forms.TextInput(attrs={'class': 'form-control'}),
            'JobName': forms.TextInput(attrs={'class': 'form-control'}),
        }





















