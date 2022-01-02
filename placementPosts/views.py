from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

jobRoles = [
    {
        'companyName': 'Amazon',
        'role' : 'SDE Intern',
        'description' : 'A SDE intern ... tasks description',
        'lastDate': '14/01/22',
        'websiteUrl' : 'www.amazon.com',
        'applyingLink': 'www.amazonjobs.com',
    },
    {
        'companyName': 'Google',
        'role' : 'Fresher SE',
        'description' : 'Fresher SE ... tasks description',
        'lastDate': '31/01/22',
        'websiteUrl' : 'www.googleApplications.com',
        'applyingLink': 'www.googlejobs.com',
    },
]

def home(request) :
    context ={
        'jobRoles' : jobRoles,
        'title' : 'Job roles - Apply soon!',
    }

    return render(request,'placementPosts/home.html',context)