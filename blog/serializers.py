from .models import Post
from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['id', 'email', 'username']

class PostsSerializer(serializers.ModelSerializer):

  class Meta:
    model = Post
    fields = [
      'id',
      'title',
      'text',
      'done',
      'created_at',
      'published_date',
    ]