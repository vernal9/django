from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from .models import Task,Entry
from .forms import TaskForm
import qr_code,qrcode
from django.views.generic import View
from django.http import JsonResponse
from mptt.forms import TreeNodeChoiceField


# Create your views here.

#create a task
def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect(reverse("tasks:task_list"))
    else:
        form = TaskForm()
    return render(request,"tasks/task_form.html",{"form":form, })


def task_list(request):
    tasks = Task.objects.all()
    return render(request,"tasks/task_list.html",{"tasks":tasks,})


def task_detail(request, pk):
    # 从url里获取单个任务的pk值，然后查询数据库获得单个对象
    task = get_object_or_404(Task, pk=pk)
    return render(request, "tasks/task_detail.html", {"task": task, })


def task_update(request, pk):
    # 从url里获取单个任务的pk值，然后查询数据库获得单个对象实例
    task_obj = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(instance=task_obj, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("tasks:task_detail", args=[pk, ]))
    else:
        form = TaskForm(instance=task_obj)
    return render(request, "tasks/task_form.html", {"form": form, "object": task_obj})

def task_delete(request, pk):
    task_obj = get_object_or_404(Task,pk=pk)
    task_obj.delete()
    return redirect(reverse("tasks:task_list"))

def yourview(request, pk):
    qrcode_url = "localhost:8000/tasks/" + str(pk)
    context = {
         qrcode_url: 'qrcode_url',
     }
    return render(request, 'task_list.html', context)

class EntryOrderView(View):
    def post(self, request):
        form = self.get_form()
        if form.is_valid():
            self.process_move(form.cleaned_data['node_id'], form.cleaned_data['target_id'], form.cleaned_data['position'])
            return JsonResponse({'success': True})
        return JsonResponse({'success': False})

    def get_form(self):
        form_data = {
            'node_id': self.request.POST.get('node_id'),
            'target_id': self.request.POST.get('target_id'),
            'position': self.request.POST.get('position'),
        }
        return EntryOrderForm(form_data)

    def process_move(self, node_id, target_id, position):
        node = Entry.objects.get(pk=node_id)
        target = Entry.objects.get(pk=target_id)
        if position == 'inside':
            node.move_to(target)
        elif position == 'before':
            node.move_to(target, 'left')
        elif position == 'after':
            node.move_to(target, 'right')

