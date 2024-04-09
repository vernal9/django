from .models import Dep
import django_filters

class DepFilter(django_filters.FilterSet):

   class Meta:
       model = Dep
       field = '__ALL__'