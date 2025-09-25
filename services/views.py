from django.shortcuts import get_object_or_404, redirect, render
from .models import Service


def service_list(request):
    services = Service.objects.all()
    return render(request, "services/list.html", {"services": services})


def service_detail(request, pk):
    service = get_object_or_404(Service, pk=pk)
    return render(request, "services/detail.html", {"service": service})


def home(request):
    return render(request, "services/home.html")
from django.shortcuts import render

# Create your views here.
