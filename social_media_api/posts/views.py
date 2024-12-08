from django.shortcuts import render

# Create your views here.


from rest_framework import viewsets
#from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from .models import Post, Comment


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