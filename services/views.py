from django.shortcuts import render, redirect
from .forms import ServiceForm
from .models import Service

# def createService(request):
#     form = ServiceForm()

#     if request.method == 'POST':
#         form = ServiceForm(request.POST)
#         if form.is_valid():
#             service.save()
#             return redirect('homepage')


def displayServices(request):
    services = Service.objects.all()
    context = {"services": services}
    return render(request, "main.html", context)


def getService(request, pk):
    service = Service.objects.get(id=pk)

    context = {"service": service}
    return render(request, "services/service.html", context)


# def updateService(request):
#     form = ServiceForm()

#     if request.method == 'POST':
#         form = ServiceForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('services')

#     context = {'form': form}
#     return render(request, 'services/service-form.html', context)


# def deleteService(request, pk):
#     service = Service.objects.get(id=pk)
#     if request.method == 'POST':
#         service.delete()
#         messages.success(request, 'Service deleted successfully!')
#         return redirect('services')

#     context = {'object': service}
#     return render(request, 'delete_template.html', context)