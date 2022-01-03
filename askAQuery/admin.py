from django.contrib import admin
from .models import Query, CommentOnQuery

# Register your models here.

admin.site.register(Query)
admin.site.register(CommentOnQuery)

