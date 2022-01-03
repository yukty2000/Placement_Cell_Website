from django.shortcuts import render
from django.http import HttpResponse
from .models import Query, CommentOnQuery
# Create your views here.



def home(request):
    queries = Query.objects.all()
    context = {
        'title' : 'Ask Away...!',
        'queries' : queries,
    }
    return render(request,'askAQuery/home.html',context)