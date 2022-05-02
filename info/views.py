from django.shortcuts import render
from .models import Tag, Info
from rest_framework import viewsets, mixins
from .permissions import UpdateOwnInfo_and_tag
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from .serializers import TagSerializer, InfoSerializer, TwoInfoSerializer



class InfoViewSet(viewsets.ModelViewSet):
	"""CRUD Price"""
	serializer_class = TwoInfoSerializer
	queryset = Info.objects.all()
	authentication_classes = (TokenAuthentication,)
	permission_classes = (UpdateOwnInfo_and_tag,)
	lookup_field = 'slug'
	filter_backends = [filters.OrderingFilter]
	ordering_fields = ['date_posted',]
	


class TagViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
	"""CRUD Price"""
	serializer_class = TagSerializer
	queryset = Tag.objects.all()
	authentication_classes = (TokenAuthentication,)
	permission_classes = (UpdateOwnInfo_and_tag,)
	lookup_field = 'slug'
