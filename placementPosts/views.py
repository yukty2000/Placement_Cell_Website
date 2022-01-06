from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import UpdateView, DeleteView
from .models import Post, CommentOnPost
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

#Posts can be made by admin only from admin site but comments are made by all users


#Function views
#List view of all placement related posts
@login_required
def listView(request) :
	#Get all posts
    posts = Post.objects.all().order_by('-datePosted')
    context ={
        'posts' : posts,
        'title' : 'Job Openings - Apply soon!',
    }

    return render(request,'placementPosts/listView.html',context)


#Detail view of a single post
@login_required
def detailView(request,pk):
	#Get specific post
	post = Post.objects.filter(id=pk).first()

	#Get all comments on post
	comments = CommentOnPost.objects.filter(post=post).order_by('-datePosted')

	context = {
		'post':post,
		'comments':comments,
		'title':post.title,
	}

	#If comment is added 
	if(request.POST):
		author=User.objects.filter(id=request.user.id).first()
		comment=request.POST.get("comment","")
		if len(comment) > 0 and len(comment)<300:
			comment_obj = CommentOnPost(author=author,comment=comment,post=post)
			comment_obj.save()
			messages.success(request,"Comment added")

		else:
			messages.error(request,"Please write comments that have greater than 0 and less than 300 characters")

		

	return render(request,'placementPosts/detailView.html',context)



#Add comment - in detail view itself


#Class views - only one model CommentOnPost
#Edit comment
class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = CommentOnPost

	fields = ['comment']

	def form_valid(self,form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	#To prevent users from updating comments written by others 
	def test_func(self):
		comment = self.get_object()
		if self.request.user == comment.author:
			return True
		return False

#Delete Comment 
class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = CommentOnPost
	success_url = '/'

	#To prevent users from deleting comments written by others 
	def test_func(self):
		comment = self.get_object()
		if self.request.user == comment.author:
			return True
		return False


