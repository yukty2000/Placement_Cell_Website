from django.urls import path
from .views import (
	CommentUpdateView,
	CommentDeleteView,
	QueryCreateView,
	QueryUpdateView,
	QueryDeleteView
)
from . import views 

urlpatterns = [
    path('', views.listView, name='placement-website-askAQuery'),
    path('query/<int:pk>/', views.detailView, name='query-detail'),
    path('query/new/', QueryCreateView.as_view(), name='query-create'),
    path('query/<int:pk>/update', QueryUpdateView.as_view(), name='query-update'),
    path('query/<int:pk>/delete', QueryDeleteView.as_view(), name='query-delete'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete', CommentDeleteView.as_view(), name='comment-delete'),

]
