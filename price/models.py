from django.db import models
from django.utils import timezone
from django.conf import settings
from django.db.models import Q
from django.urls import reverse



class PriceQuerySet(models.QuerySet):
	def mintomax(self):
		return self.order_by('price')

	def search(self, query):
		lookup= (
			Q(name__icontains=query) |
			Q(price__icontains=query) |
			Q(slug__icontains=query)
			)
		return self.filter(lookup)		



class PriceManager(models.Manager):
	def get_queryset(self):
		return PriceQuerySet(self.model, using=self._db)

	def mintomax(self):
		# self.get_queryset() is Post.objects.
		# order_by('-price') big to small
		return self.get_queryset().mintomax()

	def search(self, query=None):	
		if query is None:
			return self.get_queryset().none()
		return self.get_queryset().search(query)



class Category(models.Model):
	name= models.CharField(max_length=100)

	def __str__(self):
		return self.name

	#kinda like redirect. but more info corey pt10 28:00
	def get_absolute_url(self):
		return reverse('home')	



class Price(models.Model):
	name= models.CharField(max_length=50)
	price= models.DecimalField(max_digits= 5, decimal_places=2)
	slug= models.SlugField(unique= True, null = True, blank = True)
	date_posted= models.DateTimeField(default=timezone.now)
	author= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
	category= models.ForeignKey(Category, on_delete= models.CASCADE)

	objects= PriceManager()

	def __str__(self):
		return self.name

	#Where to go after it's been created	
	def get_absolute_url(self):		
		return reverse('home')