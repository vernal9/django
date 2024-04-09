from .models import RRequest,CheckList
from django import forms
import django_filters

class f(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = RRequest
        fields = '__all__'

class checkFilter(django_filters.FilterSet):

    class Meta:
        models = CheckList
        fields = '__all__'

