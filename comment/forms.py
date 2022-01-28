from django import forms
from comment.models import Comment


class AddCommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ("body",)
        widgets = {
            'body': forms.Textarea(attrs={'cols': 8, 'rows': 3, 'class' : 'form-control'}),
        }
    