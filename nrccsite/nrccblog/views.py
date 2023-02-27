from django.shortcuts import render

# Create your views here.
def blog(request):
	return render(request, "nrccblog/blog.html", {

		})


def single_post(request):
	return render(request, "nrccblog/single_post.html", {
		
		})