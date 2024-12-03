

from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django import forms
from .models import Post
from .models import Comment


class CustomUserCreationForm(UserChangeForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']