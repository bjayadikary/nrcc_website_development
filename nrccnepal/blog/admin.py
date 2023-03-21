from django.contrib import admin
from .models import Authors, Blogs, UserComments


class BlogsAdmin(admin.ModelAdmin):
	exclude = ['slug']

# Register your models here.
admin.site.register(Authors)
admin.site.register(Blogs, BlogsAdmin)
admin.site.register(UserComments)