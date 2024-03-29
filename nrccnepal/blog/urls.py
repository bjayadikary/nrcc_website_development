from django.urls import path
from blog import views

app_name = 'blog'
urlpatterns = [
    path("", views.blog, name="blog_page"),
	path("<slug:slug>/", views.single_blog, name="single_blog"),
	path("category/<slug:slug>/", views.categorized_blog, name='categorized_blog')

]