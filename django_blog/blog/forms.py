

from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django import forms
from .models import Post
from .models import Comment
from taggit.forms import TagField
from taggit.forms import TagWidget


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

"""
class PostForm(forms.ModelForm):
    tags = forms.CharField(required=False, help_text="Comma-separated tags")

    class Meta:
        model = Post
        fields = ['title', 'content']

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        # Process tags
        tag_names = self.cleaned_data['tags'].split(',')
        for tag_name in tag_names:
            Tag, created=Tag.objects.get_or_create(name=tag_name.strip())
            instance.tags.add(Tag)
        return instance


from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    tags = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter tags separated by commas',
        }),
        help_text="Separate tags with commas."
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        # Handle tags manually
        tag_names = self.cleaned_data['tags'].split(',')
        for tag_name in tag_names:
            tag, created = Tag.objects.get_or_create(name=tag_name.strip())
            instance.tags.add(tag)
        return instance



from django.forms import widgets


tags = forms.CharField(
    widget=widgets.Textarea(attrs={'rows': 3}),
    required=False
)
"""

from django import forms
from .models import Post

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
