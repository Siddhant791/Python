from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.

def say_hello(request):
    return HttpResponse('Hello World')