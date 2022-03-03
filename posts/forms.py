
from django import forms

from django.db.models.base import Model
from django.forms import ModelForm

from .models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['caption', 'description', 'image']