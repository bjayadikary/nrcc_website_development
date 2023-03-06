from django.shortcuts import render

# Create your views here.
def blog(request):
	return render(request, "nrccblog/blog-page.html")

def single_blog(request):
	return render(request, "nrccblog/single-blog.html")