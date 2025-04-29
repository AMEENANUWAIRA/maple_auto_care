from django.shortcuts import render, redirect
from .forms import ServiceForm

def createService(request):
    form = ServiceForm()

    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            service.save()
            return redirect('homepage')