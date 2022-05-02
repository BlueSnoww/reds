from rest_framework import serializers
from .models import Tag, Info



class InfoSerializer(serializers.ModelSerializer):
	"""Serialize Info model"""

	author_name = serializers.StringRelatedField(source= 'author', read_only=True)
	tag_name = serializers.StringRelatedField(source= 'tag', read_only=True, many=True)

	class Meta:
		model = Info
		fields = ('title', 'content', 'image', 'slug', 'author','author_name', 'tag_name', 'tag')
		lookup_field = 'slug'



class TwoInfoSerializer(serializers.ModelSerializer):
	"""Serialize Info model"""
	url = serializers.HyperlinkedIdentityField(
			view_name= 'info-detail',
			lookup_field = 'slug'
		)


	author_name = serializers.StringRelatedField(source= 'author', read_only=True)
	tag_name = serializers.StringRelatedField(source= 'tag', read_only=True, many=True)

	class Meta:
		model = Info
		fields = ('url','title', 'content', 'image', 'author','author_name', 'tag_name', 'tag')
		lookup_field = 'slug'




class TagSerializer(serializers.ModelSerializer):
	"""Serialize Tag model"""

	info = InfoSerializer(many=True, read_only=True)

	class Meta:
		model = Tag
		fields = ('name', 'info')
		lookup_field = 'slug'