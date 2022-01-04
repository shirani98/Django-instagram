from .models import Post
from django import forms
from comment.models import Comment
class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddPostForm, self).__init__(self, *args, **kwargs)
    class Meta:
        model = Post
        fields = ("body",)

class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("body",)
    