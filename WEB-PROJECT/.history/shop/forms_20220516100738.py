from django import forms

class LoginForm(forms.Form):
    mobile = forms.CharField(max_length=11)
    password = forms.CharField(max_length=20, min_length=8)