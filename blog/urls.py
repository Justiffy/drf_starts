from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'posts', views.PostViewSet) 

urlpatterns = [
    path('', include(router.urls)),
    path('posts/', include('rest_framework.urls', namespace='rest_framework'))
]