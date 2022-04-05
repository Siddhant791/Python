import datetime
from sqlite3 import Date
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .models import *


# Create your views here.

def say_hello(request):
    actor = Actor.objects.filter(first_name = 'Penelope',actor_id=1)
    paymentdo = Payment.objects.filter(payment_id = 17503)
    Actor.objects.create(first_name = 'Sid',last_name = 'Hello',last_update=datetime.datetime.now(),is_best_actor=True)
    print(actor)
    print(paymentdo)
    return HttpResponse('Hello World')