from rest_framework import serializers
from qna.models import Question, Answer



class AnswerSerializer(serializers.ModelSerializer):
	"""Serialize Answer model"""

	class Meta:
		model = Answer
		fields = ('title', 'body',  'author', )
		# https://stackoverflow.com/questions/57249850/overwriting-nested-serializers-create-method-throws-typeerror-create-got-mul
		#read_only_fields = ('question',)
		lookup_field = 'slug'
		


# https://stackoverflow.com/questions/55031552/how-to-access-child-entire-record-in-parent-model-in-django-rest-framework
class QuestionSerializer(serializers.ModelSerializer):
	"""Serialize Question model"""

	answers = AnswerSerializer(read_only=False, many=True,)

	category_name = serializers.StringRelatedField(source= 'category', read_only=True)
	
	class Meta:
		model = Question 
		fields = ('title', 'body', 'slug', 'author', 'category', 'category_name', 'answers',)
		lookup_field = 'slug'
		extra_kwargs = {
				'category': {'write_only': True},
			}



	def create(self, validated_data):

		answers_data = validated_data.pop('answers')

		question = Question.objects.create(**validated_data)

		for answer_data in answers_data:
			Answer.objects.create(question=question, **answer_data)
			return question


	def update(self, instance, validated_data):
		instance.title = validated_data.get('title', instance.title)
		instance.body = validated_data.get('body', instance.body)
		instance.slug = validated_data.get('slug', instance.slug)
		instance.author = validated_data.get('author', instance.author)
		instance.category = validated_data.get('category', instance.category)
		instance.save()
		
		# https://django.cowhite.com/blog/create-and-update-django-rest-framework-nested-serializers/
		answers_data = validated_data.pop('answers')
		answers = (instance.answers).all()
		answers = list(answers)

		for answer_data in answers_data:
			answer = answers.pop(0)
			answer.title= answer_data.get('title', answer.title)
			answer.body= answer_data.get('body', answer.body)
			answer.slug= answer_data.get('slug', answer.slug)
			answer.author= answer_data.get('author', answer.author)
			answer.question= answer_data.get('question', answer.question)
			answer.save()

		return instance