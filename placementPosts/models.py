from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

# Post can be created by admin only - so no username/author required
# Post(title,jobRole,companyName,datePosted,lastDateToApply,description,companyWebsite,applyingLink)
class Post(models.Model):

	# List view 
	title = models.CharField(max_length=200)
	jobRole = models.CharField(max_length=100)
	companyName = models.CharField(max_length=100)
	datePosted = models.DateTimeField(default=timezone.now)
	lastDateToApply = models.DateTimeField(default=timezone.now)

	# Detail view
	description = models.TextField()
	companyWebsite = models.URLField(max_length=200)
	applyingLink = models.URLField(max_length=200)
	yearOfpassing = models.IntegerField(default=2022)

	def __str__(self):
		return self.title

# Comments can be seen only in detail view of posts
# CommentOnPost(author,datePosted,comment,post)
class CommentOnPost(models.Model):

	# Only List view
	author = models.ForeignKey(User,on_delete=models.CASCADE)
	datePosted = models.DateTimeField(default=timezone.now)
	comment = models.CharField(max_length=800)
	post = models.ForeignKey(Post,on_delete=models.CASCADE)

	def get_absolute_url(self):
		return reverse('post-detail',kwargs={'pk': self.post.pk})

