from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, CommentOnPost
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def home(request) :
    posts = Post.objects.all()
    context ={
        'posts' : posts,
        'title' : 'Job roles - Apply soon!',
    }

    return render(request,'placementPosts/home.html',context)