from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .serializers import PostsSerializer
from rest_framework import viewsets

# List all posts, or create a new posts.
def post_list():

  if request.method == 'GET':
    posts = Post.objects.all()
    serializer = PostsSerializer(posts, many=True)
    return JsonResponse(serializer.data, safe=False)

# Retrieve, update or delete a post
def post_detail(request, pk):
  try:
    post = Post.objects.get(pk=pk)
  except Post.DoesNotExist:
    return HttpResponse(status=404)

  if request.method == 'GET':
    post = Post(post)
    return JsonResponse(serializer.data)

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostsSerializer