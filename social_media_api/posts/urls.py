

from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, FeedViewSet
from django.urls import path, include


router = DefaultRouter()

router.register('posts/', PostViewSet)
router.register('comments/', CommentViewSet)
router.register('feed/', FeedViewSet, basename='feaad')


urlpatterns = [
    path('', include(router.urls)),
]