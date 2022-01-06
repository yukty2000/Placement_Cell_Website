from django.urls import path
from . import views 

urlpatterns = [
    path('', views.listView, name='placement-website-askAQuery'),
]
