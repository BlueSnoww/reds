from django.shortcuts import render
from rest_framework import generics
from itertools import chain

from info.models import Info
from info.serializers import InfoSerializer

from price.models import Price 
from price.serializers import PriceSerializer

from .serializers import SearchSerializer
from rest_framework import serializers

from qna.models import Question



class SearchListView(generics.ListAPIView):
	serializer_class = SearchSerializer

	def get_queryset(self):
		query = self.request.query_params.get('q', None)
		infos = Info.objects.search(query)
		prices = Price.objects.search(query)
		questions= Question.objects.search(query= query)
		all_results = list(chain(infos, prices, questions)) 
		all_results.sort(key=lambda x: x.date_posted)


		return all_results

