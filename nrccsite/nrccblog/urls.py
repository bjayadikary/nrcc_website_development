from django.urls import path
from . import views

app_name = "nrccblog"
urlpatterns = [
	path("", views.blog, name="blog"),
]