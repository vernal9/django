from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView,UpdateView,DeleteView,ListView,TemplateView
from django.shortcuts import redirect
from django_tables2 import SingleTableView,RequestConfig
from django_filters.views import FilterView

from .models import RRequest,Extension
from .forms import RequestForm,ExtFormSet
from .tables import RequestTable
from .filters import RequestFilter
#from django.template.loader import get_template


# Create your views here.

class RequestListView(SingleTableView,FilterView):
    model = RRequest
    filter = None
    #使用  RequestFilter 進行過濾
    filterset_class = RequestFilter
    # 使用  RequestTable 顯示結果
    table_class = RequestTable
    template_name = 'rec/rrequest_list.html'

    #獲取過濾後的查詢結果
    def get_queryset(self,**kwargs):
        qs=RRequest.objects.all().order_by('-ID')
        self.filter = self.filterset_class(self.request.GET, queryset=qs)
        return self.filter.qs

    #將查詢結果與table實例結果，提供 filter和table 二個變數於 templates 顯示
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        t = self.table_class(data=self.get_queryset())
        RequestConfig(self.request,paginate={"per_page": 50}).configure(t)
        context['filter'] = self.filter
        context['table'] = t
        return context


class RequestCreateView(CreateView):
    model = RRequest
    form_class = RequestForm
    success_url = reverse_lazy('rec:rec-list')
    initial = {'Remarks':'面試主管：'}

    def get_context_data(self, **kwargs):
        context = super(RequestCreateView,self).get_context_data(**kwargs)
        context['list']=RRequest.objects.all()
        return context


class RequestUpdateView(UpdateView):
    model = RRequest
    form_class = RequestForm

    success_url = reverse_lazy('rec:rec-list')

class RequestDeleteView(DeleteView):
    model = RRequest
    success_url = reverse_lazy('rec:rec-list')

def index(request):
    num_request = RRequest.objects.all().count()

    context = {
        'num_request':num_request,

    }
    return render(request,'rec/index.html',context=context)


class ExtensionView(ListView):
    model = Extension

class ExtAddView(TemplateView):
    template_name = 'rec/ext_add.html'

    def get(self, *args, **kwargs):
        formset = ExtFormSet(queryset=Extension.objects.all())
        return self.render_to_response({'ext_formset': formset})

    def post(self,*args, **kwargs):
        formset = ExtFormSet(data=self.request.POST)

        if formset.is_valid():
             formset.save()
             return redirect(reverse_lazy("rec:ext-list"))
        return self.render_to_response({'ext_formset': formset})