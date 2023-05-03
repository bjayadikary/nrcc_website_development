from django.contrib import admin
from .models import Authors, Blogs, UserComments, TrendingBlogs, Categories


class BlogsAdmin(admin.ModelAdmin):
	exclude = ['slug']

# Register your models here.
admin.site.register(Authors)
admin.site.register(Blogs, BlogsAdmin)
admin.site.register(UserComments)
admin.site.register(TrendingBlogs)
admin.site.register(Categories)