from django.shortcuts import render
from .models import Question, Answer
from django.conf import settings
from rest_framework import viewsets
from .serializers import QuestionSerializer
from .permissions import UpdateOwnQna
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework import permissions



class QnaViewSet(viewsets.ModelViewSet):
	"""CRUD """
	serializer_class = QuestionSerializer
	queryset = Question.objects.all()
	authentication_classes = (TokenAuthentication,)
	permission_classes = (UpdateOwnQna,)
	#permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
	lookup_field = 'slug'
	filter_backends = (filters.SearchFilter,)
	search_fields = ('title', 'author__name',)
	extra_kwargs = {
		'slug': {
		'validators': []
			}
		}