from django import forms
from .utils import BootstrapFormMixin


class RegistrationForm(BootstrapFormMixin, forms.Form):
    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
    email = forms.EmailField(label='Email', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    confirm_password = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput
    )

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data['confirm_password']
        if password and confirm_password != password:
            raise forms.ValidationError('Confirm password must match password')
        return confirm_password

    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) < 8:
            raise forms.ValidationError('Minimum password length of 8 characters is required')
        return password

class LoginForm(BootstrapFormMixin, forms.Form):
    email = forms.EmailField(label='Email', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
