from django.shortcuts import render

# Create your views here.


from rest_framework import viewsets
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