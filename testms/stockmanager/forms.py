from .models import closestoack
from django import forms

class StockForm(forms.ModelForm):

    class Meta:
        model = closestoack
        fields = '__all__'