from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request) :
    return HttpResponse('<h1>Posts related to companies, available job roles, etc.!</h1>')