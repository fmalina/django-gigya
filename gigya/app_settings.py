from django.conf import settings

GIGYA_API_KEY = getattr(settings, 'GIGYA_API_KEY', 'not set')
GIGYA_SECRET_KEY = getattr(settings, 'GIGYA_SECRET_KEY', 'not set')
GIGYA_API_DOMAIN = getattr(settings, 'GIGYA_API_DOMAIN', 'us1.gigya.com')
