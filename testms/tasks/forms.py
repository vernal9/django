import mptt.forms

from .models import Task
from .models import Entry
from django import forms
from mptt.forms import MoveNodeForm
from mptt.exceptions import InvalidMove

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = '__all__'

class EntryOrderForm(forms.Form):
    node_id = forms.IntegerField()
    target_id = mptt.forms.TreeNodeChoiceField(queryset=Entry.objects.all())
    position = forms.ChoiceField(choices=[('inside', 'Inside'), ('before', 'Before'), ('after', 'After')])