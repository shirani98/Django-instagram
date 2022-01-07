from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.CharField(max_length=50)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1','password2')
           
class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'age')
        widgets = {
            'bio': forms.Textarea(attrs={'cols': 8, 'rows': 3, 'class' : 'form-control'}),
            'age': forms.TextInput(attrs={'class' : 'form-control'}),
        }
        
class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')
        widgets = {
            'first_name': forms.TextInput(attrs={'class' : 'form-control'}),
            'last_name': forms.TextInput(attrs={'class' : 'form-control'}),
        }

