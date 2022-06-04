from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    Phone = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Phone',
                                                             'class': 'form-control',
                                                             }))
    Password = forms.CharField(max_length=50,
                               required=True,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                 'class': 'form-control',
                                                                 'data-toggle': Password',
                                                                 'id': 'Password',
                                                                 'name': 'password',
                                                                 }))

    class Meta:
        model = User
        fields = ['Phone', 'Password']