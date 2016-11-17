from django.shortcuts import render
from django.http import HttpResponse
from gigya.backends.gigya import GigyaAuth


from gigya import app_settings
from gigya.forms import RegistrationForm

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
            return HttpResponse('Gigya says: %s' % r2)
    else:
        form = RegistrationForm()
    return render(request, 'gigya/account.html', {
        'api_key': app_settings.GIGYA_API_KEY,
        'form': form
    })
