from django.shortcuts import render, redirect
from .forms import CategoryFrom

# Create your views here.
def add_category(req):
    form = CategoryFrom()
    if req.method == 'POST':
        form = CategoryFrom(req.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            form.save()
            return redirect('show')
    return render(req, 'category.html', {'form':form})