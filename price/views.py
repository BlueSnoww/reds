from django.shortcuts import render
from .models import Price
from django.conf import settings
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from .serializers import PriceSerializer
from .permissions import UpdateOwnPrice
from rest_framework.permissions import IsAdminUser



class PriceViewSet(viewsets.ModelViewSet):
	"""CRUD Price"""
	serializer_class = PriceSerializer
	queryset = Price.objects.mintomax()
	authentication_classes = (TokenAuthentication,)
	permission_classes = (UpdateOwnPrice,)
	lookup_field = 'slug'

