from django import forms
from .models import Login, About

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = {'email_id', 'password', 'mobile_number', 'hint'}

class LoginForm(forms.Form):
    mob_no = forms.CharField(max_length=40)
    password = forms.CharField(max_length=35)

class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = {'about'}
        # """
        # reorder the form fields in the model form
        # """
    # def __init__(self, *args, **kwargs):
    #     super(CommentForam, self).__init__(*args, **kwargs)
    #     self.fields.keyOrder = ['username', 'title', 'message']

class ScoreForm(forms.Form):
    team1score = forms.IntegerField()
    team2score = forms.IntegerField()
