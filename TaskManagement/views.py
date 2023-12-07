from django.shortcuts import render
from tasks.models import Task
def show(req):
    form = Task.objects.all()
    return render(req, 'show.html', {'form':form})