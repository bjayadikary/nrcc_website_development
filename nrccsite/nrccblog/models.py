from django.db import models

# Create your models here.
def validate_if_between_1_10(value):
	if value <=10 and value >=0:
		return value
	else:
		raise ValidationError("This field only accepts integers between 0 and 10")


class Blogs(models.Model):
	title = models.CharField("Blog Title", max_length=500)
	body = models.TextField(default="Type here...")
	author = models.CharField(max_length=100)
	published_date = models.DateField(auto_now_add=True, blank=True)
	updated_datetime = models.DateTimeField(auto_now_add=True, blank=True)
	priority = models.IntegerField(default=0, validators=[validate_if_between_1_10])
	featured_image = models.ImageField(upload_to="images/test_uploads/", blank=True, null=True, default='default/no_image.jpg')

	def __str__(self):
		return f"{self.title}"


class Authors(models.Model):
	author = models.CharField(max_length=100)
	description = models.CharField(max_length=1000)
	author_icon = models.ImageField(upload_to="images/test_uploads/", blank=True, null=True, default='default/no_image.jpg')
	mail = models.EmailField(max_length=200)


