from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from .serializers import UserSerializer, ProfileSerializer
from .models import Position, Profile
from django.contrib.auth import get_user_model
from .permissions import UpdateOwnUser, UpdateOwnProfile



User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
	"""Handle creating, deleting and updating Users"""
	serializer_class = UserSerializer
	queryset = User.objects.all()
	authentication_classes = (TokenAuthentication,)
	permission_classes = (UpdateOwnUser,)
	filter_backends = (filters.SearchFilter,)
	search_fields = ('name', 'email',)



class UserLoginApiView(ObtainAuthToken):
   """Handle creating user authentication tokens"""
   renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES



class ProfileViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin,
						mixins.UpdateModelMixin, mixins.ListModelMixin):
	"""Handle creating user authentication tokens"""
	serializer_class = ProfileSerializer
	queryset = Profile.objects.all()	
	authentication_classes = (TokenAuthentication,)
	permission_classes = (UpdateOwnProfile,)