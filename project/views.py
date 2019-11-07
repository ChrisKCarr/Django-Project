from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import Tasks
from .forms import TaskForm


# Create your views here.
def task_list(request):
    tasks = Tasks.objects.order_by('id')
    
    form = TaskForm()
    return render(request, 'project/base.html', {'tasks': tasks, 'form': form})

def new_form(request):
    form = TaskForm()
    return render(request, 'project/form.html', {'form': form})

@require_POST
def addTask(request):
    form = TaskForm(request.POST)
    print(request.POST['text'])
    
    if form.is_valid():
        new_task = Tasks(name=request.POST['text'])
        new_task.save()
    
    return redirect('task_list')
    
def completed(request, task_id):
    task = Tasks.objects.get(pk=task_id)
    task.complete = True
    task.save()
    
    return redirect('task_list')

def deleteCompleted(request):
    Tasks.objects.filter(complete__exact=True).delete()
    
    return redirect('task_list')

def deleteAll(request):
    Tasks.objects.all().delete()
    
    return redirect('task_list') 