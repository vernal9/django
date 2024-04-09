from .models import RRequest
import django_filters

class RecFilter(django_filters.FilterSet):

    class Meta:
        model = RRequest
        fields = '__ALL__'