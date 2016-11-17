from django import forms


class RegistrationForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
    email = forms.EmailField(label='Email', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    confirm_password = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput
    )

    def clean_confirm_password(self):
        password = self.cleaned_data['password']
        confirm_passoword = self.cleaned_data['confirm_password']
        if confirm_passoword != password:
            raise forms.ValidationError('Confirm password must match password')
        return confirm_passoword