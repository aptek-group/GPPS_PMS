from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Logs

# Create your views here.
def show(request):
    logs = Logs.objects.all()
    context = {
        'head': 'Logs',
        'logs' : logs
    }
    return render(request, 'logs/logs.html', context)
