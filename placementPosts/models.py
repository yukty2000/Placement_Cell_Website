from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

# Post can be created by admin only - so no username/author required
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

	def __str__(self):
		return self.title

# Comments can be seen only in detail view of posts
class CommentOnPost(models.Model):

	# Only List view
	author = models.ForeignKey(User,on_delete=models.CASCADE)
	datePosted = models.DateTimeField(default=timezone.now)
	comment = models.CharField(max_length=800)
	post = models.ForeignKey(Post,on_delete=models.CASCADE)

	

