from django.urls import path
from . import views

app_name = "nrccblog"
urlpatterns = [
	path("", views.blog, name="blog"),
	path("single-post/", views.single_post, name="single_post"),

]
