from django.shortcuts import render
from gigya import app_settings

def index(request):
    return render(request, 'gigya/index.html', {
        'api_key': app_settings.GIGYA_API_KEY
    })


def account(request):
    return render(request, 'gigya/registration.html', {
        'api_key': app_settings.GIGYA_API_KEY
    })
