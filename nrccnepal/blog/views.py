from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger
from django.contrib import messages
from django.template.defaultfilters import slugify
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Blogs, TrendingBlogs, Categories
from .forms import CommentForm
from datetime import date


# Create your views here.

def blog(request):
	# Retriving the top blogs with highest priority
	trending_blogs = TrendingBlogs.objects.all().order_by('priority')

	# Retreiving categories
	categories = Categories.objects.all()

	all_blogs = Blogs.objects.all().order_by('priority','-updated_datetime','-published_date')
	paginator = Paginator(all_blogs, 4) # number of objects to display per page
	current_page = request.GET.get('page') # retreives current page number

	try:
		paginator_objects = paginator.page(current_page)
	except PageNotAnInteger:
		paginator_objects = paginator.page(1)

	return render(request, "blog/blog-page.html", {
		"blogs" : paginator_objects,
		"trending_blogs": trending_blogs,
		"categories": categories,
		})


def categorized_blog(request, slug):
	# Retriving the top blogs with highest priority
	trending_blogs = TrendingBlogs.objects.all().order_by('priority')

	# Retrieving all categories for category tab
	categories = Categories.objects.all()

	# Getting the category object (id) based on the category name
	category_obj = get_object_or_404(Categories, slug=slug)

	filtered_blogs = category_obj.category_blog.all().order_by('priority', '-updated_datetime', '-published_date') # using related_name
	paginator = Paginator(filtered_blogs, 4) # number of objects to display per page
	current_page = request.GET.get('page') # retreives current page number

	try:
		paginator_objects = paginator.page(current_page)
	except PageNotAnInteger:
		paginator_objects = paginator.page(1)

	return render(request, "blog/blog-page.html", {
		"blogs" : paginator_objects,
		"trending_blogs": trending_blogs,
		"categories": categories,
		})

def single_blog(request, slug):
	blog = Blogs.objects.get(slug=slug) # Handle exception Blogs.DoesNotExist

	# Retreiving categories
	categories = Categories.objects.all()

	if request.method == "POST":
		comment_form = CommentForm(request.POST)
		if comment_form.is_valid():
			comment = comment_form.save(commit=False)
			comment.blogs = blog
			comment.date = date.today() # timezone.now()
			comment.save()
			return HttpResponseRedirect(reverse("blog:single_blog", args=[slug]))
	else:
		comment_form = CommentForm()

	# Retriving the top blogs with highest priority
	trending_blogs = TrendingBlogs.objects.all().order_by('priority')

	# Retrieving user comments of particular blog
	comments = blog.blog_comment.all()

	return render(request, "blog/single-blog.html", {
		"blog" : blog,
		"trending_blogs" : trending_blogs,
		"comments" : comments,
		"comment_form" : comment_form,
		"categories": categories,
		})
