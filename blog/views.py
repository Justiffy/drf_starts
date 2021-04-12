from .models import Post
from .serializers import PostsSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, mixins, generics

class PostList(APIView):
    # List all posts, or create a new posts.
    queryset = Post.objects.all()
    serializer_class = PostsSerializer

    def get(self, request, format = None):
      posts = Post.objects.all()
      serializer = PostsSerializer(posts, many=True)
      return Response(serializer.data)

    def post(self, request, format = None):
      serializer = PostsSerializer(data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
      return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class PostDetail(mixins.RetrieveModelMixin, 
                mixins.UpdateModelMixin, 
                mixins.DestroyModelMixin,
                generics.GenericAPIView):
  # Retrieve, update or delete a post instance.
  queryset = Post.objects.all()
  serializer_class = PostsSerializer

  def get(self, request, *args, **kwargs):
    return self.retrieve(request, *args, **kwargs)

  def put(self, request, *args, **kwargs):
    return self.update(request, *args, **kwargs)

  def patch(self, request, *args, **kwargs):
    return self.partial_update(request, *args, **kwargs)

  def delete(self, request, *args, **kwargs):
    return self.destroy(request, *args, **kwargs)