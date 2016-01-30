from django import forms
from .models import Users, Comments

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = {'username', 'password'}

class LoginForm(forms.Form):
    username = forms.CharField(max_length=10)
    password = forms.CharField(max_length=10)
