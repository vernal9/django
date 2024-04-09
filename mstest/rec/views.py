import django_tables2
from django.shortcuts import render
from django.views.generic import ListView, DetailView,UpdateView,CreateView
from django.urls import reverse_lazy
from .models import RRequest,Depment,ServerValue,CheckList
from .forms import RRequestForm,RequestCreateForm,RequestFinishUpdate
from .tables import ServerValueTable
from django_tables2.views import SingleTableMixin,RequestConfig,SingleTableView
from .filters import checkFilter
import pandas as pd

from .filters import f

# Create your views here.


class RRequestListView(ListView):
    model = RRequest
    queryset = RRequest.objects.filter(IsFinished=0)
    template_name = 'rec/rec_list.html'


class RRequestCreateView(CreateView):
    form_class = RequestCreateForm
    model = RRequest
    #fields = '__all__'
    template_name = 'rec/rec_create.html'

class RRequestFinUpdateView(UpdateView):
    form_class = RequestFinishUpdate
    model = RRequest
    #fields = ['IsFinished']
    template_name = 'rec/rec_finupdate.html'
    queryset = RRequest.objects.all()

#class ServerValueListView(ListView):
#    model = ServerValue
#    table_class = ServerValueTable
#    template_name = 'rec/todolist.html'

class ServerValueListView(django_tables2.SingleTableView):
    table_class = ServerValueTable
    queryset = ServerValue.objects.all()
    template_name = "rec/todolist.html"


class checkListView(ListView):
    model = CheckList
    queryset = CheckList.objects.filter(Checked=0)
    template_name = "rec/checklist.html"

def home(request):
    item = RRequest.objects.all().values()
    df = pd.DataFrame(item)
    mydict = {
        "df": df.to_html()
    }
    return render(request, 'rec/pd.html', context=mydict)












