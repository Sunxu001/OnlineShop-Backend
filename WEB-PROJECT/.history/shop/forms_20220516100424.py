from django import forms

class LoginForm(forms.Form):
    mobile = models.CharField(max_length=11, verbose_name="phone number", default="")