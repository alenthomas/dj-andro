from django import forms
from .models import Users, Comments

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = {'username', 'password'}
