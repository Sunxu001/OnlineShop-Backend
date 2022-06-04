from django import forms

class LoginForm(forms.Form):
    mobile = models.CharField(max_length=11)