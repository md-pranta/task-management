from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import Task
# Create your views here.
def add_task(req):
    form = TaskForm()
    if req.method == 'POST':
        form = TaskForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('show')
    return render(req, 'task.html', {'form':form})
def edit_task(req, id):
    data = Task.objects.get(pk=id)
    form = TaskForm(instance=data)
    if req.method == 'POST':
        form = TaskForm(req.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('show')
    return render(req, 'task.html', {'form':form})
def delete(req, id):
    data = Task.objects.get(pk=id)
    data.delete()
    return redirect('show')