from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):
	if request.method == 'POST' :
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request,f'Account created for {username}. Login!')
			return redirect('login')
	else :
		form = UserRegisterForm()
	

	return render(request,'users/register.html',context={'form':form,'title':'Register'})


@login_required
def profile(request):
	if request.method == 'POST' :
		form = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile)
		if form.is_valid():
			form.save()
			messages.success(request,f'Profile successfully updated for {request.user.username}.')
			return redirect('profile')
	else :
		form = ProfileUpdateForm(instance = request.user.profile)
	

	context = {
		'form':form
	}

	return render(request,'users/profile.html',context)