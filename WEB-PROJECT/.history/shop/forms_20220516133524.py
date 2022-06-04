from django import forms

class LoginForm(forms.Form):
    class UserForm(ModelForm):
    class Meta:
        model = User