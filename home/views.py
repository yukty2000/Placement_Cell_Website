from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Templates will have about the cell and Hall of fame
def home(request) :
    context = {
        'title': 'HITK Placement Cell',
    }
    return render(request,'home/home.html',context)


