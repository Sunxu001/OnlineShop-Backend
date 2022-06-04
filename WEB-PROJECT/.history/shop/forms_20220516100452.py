from django import forms

class LoginForm(forms.Form):
    mobile = f.CharField(max_length=11)