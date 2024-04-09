import datetime
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput
from .models import RRequest,Extension
from django import forms
from datetime import date


class RequestForm(forms.ModelForm):

    class Meta:
        model = RRequest
        fields = '__all__'
        InterviewTime = forms.DateTimeField(input_formats=['%Y/%m/%d %H:%M'])
        widgets = {
            'InterviewTime': DateTimePickerInput(format='%Y/%m/%d %H:%M'),
        }


    #欄位驗證檢核
    def clean_RecruitRequestComment(self):
        Num104 = self.cleaned_data['RecruitRequestComment']
        rc = self.cleaned_data['RecruitRequestType']
        if rc == 0 and len(Num104)<3:
           raise  forms.ValidationError('來源類型為「人力銀行」，需填寫「履歷編號」！')
        return Num104

# formset 設定
ExtFormSet = forms.modelformset_factory(
    Extension,fields=('code','num'),extra=4,can_delete=True
)

