from django import forms

class LoginForm(forms.Form):
    class Meta:
        model = Login