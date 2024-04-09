from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render,redirect
from .models.Recruit_Request import Recruit_Request
from .forms import RRequestForm
from django_tables2 import SingleTableView,RequestConfig
from django_filters.views import FilterView
from hrbasic.models import *

# table.py定义了用哪些字段将在表格中展示
from .table import RRList

import django_tables2 as tables


# Create your views here.

def index(request):

    rrall = Recruit_Request.objects.filter(IsFinished=0)
    form = RRequestForm()

    if request.method == "POST":
        form = RRequestForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/rec")

    context = {
        'rrall': rrall,
        'form': form
    }
    return render(request, 'rec/index.html', context)


def rrupdate(request,pk):
    rrall = Recruit_Request.objects.get(ID=pk)

    form = RRequestForm(instance=rrall)

    context = {
        'form':form
    }
    return render(request,'rec/rrupdate.html',context)


class RRTableView(tables.SingleTableView):
     table_class = RRList
     queryset = Recruit_Request.objects.filter(IsFinished=0)
     template_name = "rec/rrlist.html"

def calendar(request):
    events = Recruit_Request.objects.all()

    context = {
        "events": events,
    }

    return render(request,'rec/calendar.html', context)

def add_event(request):
    start = request.GET.get("start", None)
    title = request.GET.get("title", None)
    new_event = Events(event_name=str(title), start_date=start)
    new_event.save()	# 保存到数据库
    data = {}
    return JsonResponse(data)


















