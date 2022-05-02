from django.db import models
from django.conf import settings
from django.db.models import Q
from django.utils import timezone
from django.urls import reverse



class QnAQuerySet(models.QuerySet):
	def search(self, query):
		lookup= (
				Q(title__icontains=query) |
				Q(body__icontains=query) |
				Q(slug__icontains=query)  
				)	
		return self.filter(lookup)



class QnAManager(models.Manager):
	def get_queryset(self):
		return QnAQuerySet(self.model, using=self._db)

	def search(self, query=None):
		if query is None:
			return self.get_queryset().none()
		return self.get_queryset().search(query)	



class Category(models.Model):
	name= models.CharField(max_length=100)

	def __str__(self):
		return self.name



class Question(models.Model):
	title= models.CharField(max_length= 100)
	body= models.TextField()
	slug= models.SlugField(unique= True)
	date_posted= models.DateTimeField(default=timezone.now)
	author= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE, related_name = 'questions')
	category= models.ForeignKey(Category, on_delete= models.CASCADE, related_name = 'questions')

	objects= QnAManager()
	
	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('home')

	

class Answer(models.Model):
	title= models.CharField(max_length= 100)
	body= models.TextField()
	slug= models.SlugField(unique= True)
	date_posted= models.DateTimeField(default=timezone.now)
	author= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE, related_name = 'answers')
	question= models.ForeignKey(Question, on_delete= models.CASCADE, related_name = 'answers')
	
	objects= QnAManager()

	def __str__(self):
		return self.title

	def get_absolute_url(self):	
		return reverse('home')