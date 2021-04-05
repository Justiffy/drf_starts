from .models import Post
from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    username = serializers.CharField(max_length=100)

class PostsSerializer(serializers.HyperlinkedModelSerializer):
  author = UserSerializer() 
  class Meta:
    model = Post
    fields = [
      'id',
      'title',
      'text',
      'done',
      'author',
      'created_at',
      'published_date',
    ]