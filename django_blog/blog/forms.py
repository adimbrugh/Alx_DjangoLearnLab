

from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from taggit.forms import TagField
from taggit.forms import TagWidget
from .models import Comment
from django import forms
from .models import Post





class CustomUserCreationForm(UserChangeForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



class PostForm(forms.ModelForm):
    tags = TagField(required=False) 
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']



class PostForm(forms.ModelForm):
    tags = forms.CharField(
        required=False,
        widget=TagWidget(),  # Custom widget for tags
        help_text="Separate tags with commas."
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        # Handle tags manually if not using django-taggit
        tag_names = self.cleaned_data['tags'].split(',')
        for tag_name in tag_names:
            tag, created = Tag.objects.get_or_create(name=tag_name.strip())
            instance.tags.add(tag)
        return instance
