from django.shortcuts import render
from django.http import HttpResponse


def hello(request):
    context = {}
    return render(request, 'index.html', context)
