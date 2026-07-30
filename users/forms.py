from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import ModelForm

from .models import User

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')

class UserLoginForm(AuthenticationForm):
    username = forms.EmailField(label='Email')

class UserProfileForm(ModelForm):
    class Meta:
        model = User
        fields = ('email', 'avatar', 'phone_number', 'country')