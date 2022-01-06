from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Query, CommentOnQuery
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

#List view of all queries
@login_required
def listView(request):
    queries = Query.objects.all().order_by('-datePosted')
    context = {
        'title' : 'Queries',
        'queries' : queries,
    }
    return render(request,'askAQuery/listView.html',context)


#Detail view of a single query
@login_required
def detailView(request,pk):
	#Get specific query
	query = Query.objects.filter(id=pk).first()

	#Get all replies on query
	replies = CommentOnQuery.objects.filter(query=query).order_by('-datePosted')

	context = {
		'query':query,
		'replies':replies,
		'title':query.question,
	}

	#If reply is added 
	if(request.POST):
		author=User.objects.filter(id=request.user.id).first()
		reply=request.POST.get("reply","")
		if len(reply) > 0 and len(reply)<300:
			reply_obj = CommentOnQuery(author=author,comment=reply,query=query)
			reply_obj.save()
			messages.success(request,"Reply added")

		else:
			messages.error(request,"Please write replies that have greater than 0 and less than 300 characters")

		

	return render(request,'askAQuery/detailView.html',context)

#Class views - only one model Query
#Create queries
class QueryCreateView(LoginRequiredMixin, CreateView):
	model = Query

	fields = ['question','description']

	def form_valid(self,form):
		form.instance.author = self.request.user
		return super().form_valid(form)

#Update queries	
class QueryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Query

	fields = ['question','description']

	def form_valid(self,form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	#To prevent users from updating queries written by others 
	def test_func(self):
		query = self.get_object()
		if self.request.user == query.author:
			return True
		return False

#Delete queries
class QueryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Query
	success_url = '/askAQuery/'

	#To prevent users from deleting queries written by others 
	def test_func(self):
		query = self.get_object()
		if self.request.user == query.author:
			return True
		return False

#Add reply - in detail view itself

#Class views - only one model CommentOnQuery
#Edit comment
class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = CommentOnQuery

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
	model = CommentOnQuery
	success_url = '/askAQuery/'

	#To prevent users from deleting comments written by others 
	def test_func(self):
		comment = self.get_object()
		if self.request.user == comment.author:
			return True
		return False
