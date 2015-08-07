from django.shortcuts import render
from django.http import HttpResponse
import Quandl

def home(request):
    return HttpResponse("Hello, there. Welcome.")
