import uuid
import os
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.conf import settings
from django.urls import reverse
from django.db.models import Q



class InfoQuerySet(models.QuerySet):
	def is_public(self):
		return self.filter(public=True)

	def search(self, query):
		lookup= (
			Q(title__icontains=query) |
			Q(content__icontains=query) |
			Q(slug__icontains=query)
			)
		return self.is_public().filter(lookup).order_by('-date_posted')			


class InfoManager(models.Manager):
	def get_queryset(self):
		return InfoQuerySet(self.model, using=self._db)

	def is_public(self):
		# self.get_queryset() is Post.objects.
		return self.get_queryset().is_public()	

	def search(self, query=None):	
		if query is None:
			return self.get_queryset().none()
		return self.get_queryset().search(query)



#DRF advance
def info_image_file_path(instance, filename):
    """Generate file path for new recipe image"""
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join(settings.BASE_DIR, 'media', 'info_img', filename)    



class Tag(models.Model):
	name= models.CharField(unique=True, max_length=100)

	def __str__(self):
		return self.name

	#kinda like redirect. but more info corey pt10 28:00
	def get_absolute_url(self):
		return reverse('home')	



class Info(models.Model):
    title = models.CharField(max_length=120)
    content= models.TextField(null=True, blank= True) 
    image= models.ImageField(upload_to= info_image_file_path,null=True, blank= True)
    slug= models.SlugField(unique= True, null = True, blank = True)
    date_posted= models.DateTimeField(default=timezone.now)
    updated= models.DateTimeField(auto_now=True)
    author= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
    tag = models.ManyToManyField(Tag, blank = True, related_name='info')
    public = models.BooleanField(default=True)
    
    objects= InfoManager()


    def is_public(self):
        return self.public

    def __str__(self):
        return self.title
