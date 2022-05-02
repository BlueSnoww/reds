from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from .models import Profile


User = get_user_model()


#When a user is created, create profile
@receiver(post_save, sender= User)
def create_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)



#When a user is saved, create profile
@receiver(post_save, sender= User)
def save_profile(sender, instance, **kwargs):
	instance.profiles.save()