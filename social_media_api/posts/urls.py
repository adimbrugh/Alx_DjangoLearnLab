

from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, FeedViewSet, like_post, unlike_post
from django.urls import path, include


router = DefaultRouter()

router.register('posts/', PostViewSet)
router.register('comments/', CommentViewSet)
router.register('feed/', FeedViewSet, basename='feaad')


urlpatterns = [
    path('', include(router.urls)),
    path('<int:pk>/like/', like_post, name='like_post'),
    path('<int:pk>/unlike/', unlike_post, name='unlike_post'),
]