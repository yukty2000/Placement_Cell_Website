from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, CommentOnPost
# Create your views here.


def home(request) :
    posts = Post.objects.all()
    context ={
        'posts' : posts,
        'title' : 'Job roles - Apply soon!',
    }

    return render(request,'placementPosts/home.html',context)