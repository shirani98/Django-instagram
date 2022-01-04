from .models import Post
from django import forms

class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddPostForm, self).__init__(self, *args, **kwargs)
    class Meta:
        model = Post
        fields = ("body",)