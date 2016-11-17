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
            r = api.request('accounts.register', {
                'username': d['email'],
                'email': d['email'],
                'password': d['password'],
                'regToken': 'foo.bar'
            })
            return HttpResponse('Gigya says: %s' % r.getResponseText())
    else:
        form = RegistrationForm()
    return render(request, 'gigya/account.html', {
        'api_key': app_settings.GIGYA_API_KEY,
        'form': form
    })
