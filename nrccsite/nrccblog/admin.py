from django.contrib import admin
from .models import Authors, Blogs, UserComments

# Register your models here.
admin.site.register(Authors)
admin.site.register(Blogs)
admin.site.register(UserComments)