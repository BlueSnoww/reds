from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from info.models import info_image_file_path



class UserManager(BaseUserManager):
	"""Manager for user profiles"""

	def create_user(self, email, name, password=None):
		"""Create a new user profile"""
		if not email:
			raise ValueError('Users must have an email address')

		email = self.normalize_email(email)
		user = self.model(email=email, name=name)

		user.set_password(password)
		user.save(using=self._db)

		return user

	def create_superuser(self, email, name, password):
		"""Create and save a new superuser with given details"""
		user = self.create_user(email, name, password)

		user.is_superuser = True
		user.is_staff = True
		user.save(using=self._db)

		return user



class User(AbstractBaseUser, PermissionsMixin):
	"""Database model for users in the system"""
	email = models.EmailField(max_length=255, unique=True)
	name = models.CharField(max_length=255)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)

	objects = UserManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['name']

	def get_full_name(self):
		"""Retrieve full name for user"""
		return self.name

	def get_short_name(self):
		"""Retrieve short name of user"""
		return self.name

	def __str__(self):
		"""Return string representation of user"""
		return self.name



class Position(models.Model):
	name= models.CharField(max_length=100)

	def __str__(self):
		return self.name



class Profile(models.Model):
	position = models.ForeignKey(Position, on_delete= models.CASCADE, null=True, blank= True)
	about_you = models.CharField(max_length=255, blank=True, default='')
	user= models.OneToOneField(settings.AUTH_USER_MODEL, on_delete= models.CASCADE, related_name = 'profiles')
	image= models.ImageField(upload_to= info_image_file_path,null=True, blank= True)

	def __str__(self):
		return f'{self.user.name} Profile'