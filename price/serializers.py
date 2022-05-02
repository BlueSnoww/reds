from rest_framework import serializers

from .models import Price



class PriceSerializer(serializers.ModelSerializer):
	"""Serialize Price model"""

	class Meta:
		model = Price
		fields = ('name', 'price', 'slug', 'author', 'category')
		lookup_field = 'slug'
		