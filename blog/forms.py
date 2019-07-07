from django import forms

from .models import BlogPost, Comment


class BlogPostForm(forms.ModelForm):

    class Meta:
        model = BlogPost
        fields = ['title', 'content']


class CommentForm(forms.ModelForm):
    comment = forms.CharField(label='', widget=forms.Textarea(attrs={
        'rows': 3,
        'placeholder': 'Please leave a comment...'
        }))
    class Meta:
        model = Comment
        fields = ['comment']
