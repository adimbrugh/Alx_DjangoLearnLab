from django.shortcuts import render

# Create your views here.


from rest_framework import viewsets, generics
from rest_framework.viewsets import ViewSet
from .serializers import PostSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from .models import Post, Comment
from rest_framework.response import Response


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return [permissions.IsAuthenticated(), permissions.IsOwner()]
        return [permissions.IsAuthenticated()]



class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return [permissions.IsAuthenticated(), permissions.IsOwner()]
        return [permissions.IsAuthenticated()]
    


class FeedViewSet(ViewSet):
    queryset = Post.objects.all()  # Add this if not present
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request):
        followed_users = request.user.following.all()
        posts = Post.objects.filter(author__in=followed_users).order_by('-created_at')
        serializer = self.serializer_class(posts, many=True)
        return Response(serializer.data)

    def get(self, request, *args, **kwargs):
        # Get the currently authenticated user
        user = request.user
        
        # Fetch the users the authenticated user is following
        following_users = user.following.all()  # Adjust this based on your model's `related_name`
        
        # Fetch posts authored by those users, ordered by creation date
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
        
        # Serialize the posts
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    




# posts/views.py
"""
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Like, Post
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_post(request, pk):
    post = Post.objects.get(id=pk)
    if Like.objects.filter(user=request.user, post=post).exists():
        return Response({'detail': 'You have already liked this post.'}, status=status.HTTP_400_BAD_REQUEST)

    Like.objects.create(user=request.user, post=post)

    notification = Notification(
        recipient=post.author,
        actor=request.user,
        verb='liked your post',
        target_content_type=ContentType.objects.get_for_model(Post),
        target_object_id=post.id
    )
    notification.save()

    return Response({'detail': 'Post liked successfully.'}, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unlike_post(request, pk):
    post = Post.objects.get(id=pk)
    like = Like.objects.filter(user=request.user, post=post).first()
    if not like:
        return Response({'detail': 'You have not liked this post.'}, status=status.HTTP_400_BAD_REQUEST)

    like.delete()

    return Response({'detail': 'Post unliked successfully.'}, status=status.HTTP_200_OK)
"""


from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Post, Like
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_post(request, pk):
    # Retrieve the post or return a 404 if not found
    post = generics.get_object_or_404(Post, pk=pk)

    # Check if the user has already liked the post
    like, created = Like.objects.get_or_create(user=request.user, post=post)

    if not created:
        return Response({'detail': 'You have already liked this post.'}, status=status.HTTP_400_BAD_REQUEST)

    # Create a notification for the post author when a user likes the post
    Notification.objects.create(
        recipient=post.author,
        actor=request.user,
        verb='liked your post',
        target_content_type=ContentType.objects.get_for_model(Post),
        target_object_id=post.id
    )

    return Response({'detail': 'Post liked successfully.'}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unlike_post(request, pk):
    # Retrieve the post or return a 404 if not found
    post = generics.get_object_or_404(Post, pk=pk)

    # Check if the user has liked the post
    like = Like.objects.filter(user=request.user, post=post).first()

    if not like:
        return Response({'detail': 'You have not liked this post.'}, status=status.HTTP_400_BAD_REQUEST)

    # Delete the like
    like.delete()

    return Response({'detail': 'Post unliked successfully.'}, status=status.HTTP_200_OK)