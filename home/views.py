from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Templates will have about the cell and Hall of fame
def home(request) :
    return HttpResponse('<h1>Placement Cell</h1>')


