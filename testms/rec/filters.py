import django_filters
from .models import RRequest
from django.db.models import Q

class RequestFilter(django_filters.FilterSet):

    #自定義過瀘字段
    query = django_filters.CharFilter(method='my_request_filter',label='關鍵字')

    def my_request_filter(self,queryset,q,value):
        return queryset.filter(Q(CandidatesName__icontains=value) | Q(JobName__icontains=value))

    class Meta:
        model = RRequest
        fields = {
            'IsFinished',
            'RecruitStatus',
            'JobName'
        }