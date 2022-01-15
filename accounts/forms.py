from django import forms
from .models import MyUser
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class UserRegisterForm(UserCreationForm):
    phone = forms.CharField(max_length=50)
    class Meta:
        model = MyUser
        fields = ('username', 'email','phone', 'password1','password2')
    def clean_phone(self):
        data = self.cleaned_data['phone']
        if len(data) == 11:
            return data
        else :
            raise ValidationError("your phone incorrect")
    def clean_email(self):
        data = self.cleaned_data['email']
        user = MyUser.objects.filter(email = data).exists()
        if user:
            raise ValidationError("User with this Email already exists.")
        return data

           
class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ('first_name','last_name', 'bio','phone', 'age','avatar')
        
        
