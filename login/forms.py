from django import forms
from .models import Users, Comments

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = {'username', 'password'}

class LoginForm(forms.Form):
    username = forms.CharField(max_length=10)
    password = forms.CharField(max_length=10)

class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = {'username', 'title', 'message'}
        """
        reorder the form fields in the model form
        """
    def __init__(self, *args, **kwargs):
        super(AddCommentForm, self).__init__(*args, **kwargs)
        self.fields.keyOrder = ['username', 'title', 'message']
