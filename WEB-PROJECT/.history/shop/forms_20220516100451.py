from django import forms

class LoginForm(forms.Form):
    mobile = .CharField(max_length=11)