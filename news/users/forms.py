from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from users.models import CustomUser


class CustomUserCreationFrom(UserCreationForm):
    
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'age')


class CustomUserChangeForm(UserChangeForm):
    
    class Meta:
        model = CustomUser
        fields = ('username','email','age',)
        