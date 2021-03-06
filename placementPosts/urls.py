from django.urls import path
from .views import (
	CommentUpdateView,
	CommentDeleteView
)
from . import views 


urlpatterns = [
    path('', views.listView, name='placement-website-posts'),
    path('post/<int:pk>/',views.detailView, name='post-detail'),
    path('post/<int:fk>/comment/<int:pk>/update',CommentUpdateView.as_view(), name='pcomment-update'),
    path('post/<int:fk>/comment/<int:pk>/delete',CommentDeleteView.as_view(), name='pcomment-delete'),
]

