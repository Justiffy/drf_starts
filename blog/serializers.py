from .models import Post
from rest_framework import serializers

class PostsSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Post 
    fields = [
      # 'id',
      # 'title',
      # 'text',
      # 'done',
      'author',
      # 'created_at',
      # 'published_date',
    ]