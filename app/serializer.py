from rest_framework import serializers
from .models import Profile, Course, Note
from cloudinary.models import CloudinaryField
# user
from django.contrib.auth.models import User


# get all users
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name','date_joined')

# create user
class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

# Subject serializer
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ("id","name", "created_at", "updated_at")


# Notes serializer
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ("id","user", "title", "description", "subject", "created_at", "updated_at")


# Profile serializer
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("user", "bio", "profile_pic", "notes", "created_at", "updated_at")