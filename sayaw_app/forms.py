from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUser


class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    staff = forms.BooleanField(label='Staff', required=False, initial=False, widget=forms.CheckboxInput)
    superadmin = forms.BooleanField(label='Super Admin', required=False, initial=False, widget=forms.CheckboxInput)



class loginForm(AuthenticationForm):
    pass 
