from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Query(models.Model):

	# List view 
	question = models.CharField(max_length=500)
	author = models.ForeignKey(User,on_delete=models.CASCADE)
	datePosted = models.DateTimeField(default=timezone.now)

	# Detail view
	description = models.TextField()

	def __str__(self):
		return self.question

# Comments can be seen only in detail view of query
class CommentOnQuery(models.Model):

	# Only List view
	author = models.ForeignKey(User,on_delete=models.CASCADE)
	datePosted = models.DateTimeField(default=timezone.now)
	comment = models.CharField(max_length=800)
	query = models.ForeignKey(Query,on_delete=models.CASCADE)


