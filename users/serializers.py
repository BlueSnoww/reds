from rest_framework import serializers
from django.contrib.auth import get_user_model
from users import models
from .models import Position, Profile



User = get_user_model()



class UserSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = User
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """Create and return a new user"""
        user = User.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user

    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)



class ProfileSerializer(serializers.ModelSerializer):
	"""Serialize Profile Model"""

	id = serializers.IntegerField(read_only=True)
	user_name = serializers.CharField(source='user.name', read_only=True)
	user_email = serializers.EmailField(source='user.email', read_only=True)
	position_name = serializers.StringRelatedField(source= 'position', read_only=True)
	#user_id = serializers.ReadOnlyField(source='user.id')
	

	class Meta:
		model = Profile
		fields = ('id', 'user_name', 'user_email', 'position_name', 'about_you', 'image',)

