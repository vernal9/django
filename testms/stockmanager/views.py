from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from django.urls import reverse_lazy
from django.views.generic import CreateView,UpdateView,DeleteView,ListView
from .models import closestoack
from django.db.models import Sum,F,Window

# Create your views here.

class ClosestockListView(ListView):
    model = closestoack
    fields = ['close_sn','close_id', 'close_size', 'close_number', 'close_employee']
    context_object_name = 'closelist'


    def get_context_data(self,  **kwargs):
        context = super(ClosestockListView, self).get_context_data(**kwargs)
        context['sum_list']=closestoack.objects.values('close_id', 'close_size').annotate(
         total=Sum('close_number')).order_by('total')
        return context

class ClosestockUpdate(UpdateView):
    model = closestoack
    fields = ['close_sn','close_id', 'close_size', 'close_number', 'close_employee']
    success_url = reverse_lazy('stockmanager:closestock_list')

class ClosestockDelete(DeleteView):
    model = closestoack
    fields = ['close_id', 'close_size', 'close_number', 'close_employee']
    success_url = reverse_lazy('stockmanager:closestock_list')

class ClosestockCreateView(CreateView):
    model = closestoack
    fields = ['close_id','close_size','close_number','close_employee']

    initial = {'close_employee':'T18026'}
    success_url = reverse_lazy('stockmanager:closestock_list')
    
    def form_valid(self, form):
        return super(ClosestockCreateView, self).form_valid(form)

    #def get_context_data(self, **kwargs):
    #    context = super(ClosestockCreateView,self).get_context_data(**kwargs)
    #    context['list']=closestoack.objects.all()
    #    return context