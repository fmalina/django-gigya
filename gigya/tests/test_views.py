from django.shortcuts import render
from django.http import HttpResponse
from gigya.backends.gigya import GigyaAuth


from gigya import app_settings
from gigya.forms import (
    RegistrationForm,
    LoginForm,
)

def index(request):
    return render(request, 'gigya/index.html', {
        'api_key': app_settings.GIGYA_API_KEY
    })


def account(request):
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            d = form.cleaned_data
            api = GigyaAuth()
            get_token = api.request('accounts.initRegistration', {})
            token = get_token.data['regToken']
            r2 = api.request('accounts.register', {
                'email': d['email'],
                'password': d['password'],
                'regToken': token
            })
            errorCode = r2.data['errorCode']
            if errorCode == GigyaAuth.ERROR_CODE_SUCCESS:
                return render(request, 'gigya/registration-success.html')
            else:
                if errorCode == GigyaAuth.ERROR_CODE_VALIDATION:
                    for error_details in r2.data['validationErrors']:
                        if error_details['errorCode'] == GigyaAuth.ERROR_CODE_UNIQUE_IDENTIFIER_EXISTS:
                            field_name = error_details['fieldName']
                            if field_name == 'email':
                                form.add_error('email', 'Email already exists')
    else:
        form = RegistrationForm()
    return render(request, 'gigya/account.html', {
        'api_key': app_settings.GIGYA_API_KEY,
        'form': form
    })


def login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            return HttpResponse('Logging in')
    else:
        form = LoginForm()
    return render(request, 'gigya/login.html', {
        'form': form
    })
