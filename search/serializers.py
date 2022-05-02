from rest_framework import serializers
from info.models import Info
from info.serializers import InfoSerializer

from price.models import Price
from price.serializers import PriceSerializer

from qna.models import Question, Answer
from qna.serializers import QuestionSerializer, AnswerSerializer

#from users.serializers import UserSerializer

#from django.contrib.auth import get_user_model



class SearchSerializer(serializers.Serializer):
	"""Serialize searches"""

	def to_representation(self, obj):
		if isinstance(obj, Info):
			serializer = InfoSerializer(obj)
		elif isinstance(obj, Price):
			serializer = PriceSerializer(obj)
		elif isinstance(obj, Question):
			serializer = QuestionSerializer(obj)
		else:
			raise Exception("Neither instance!")
		return serializer.data



