from django.conf import settings

GIGYA_API_KEY = getattr(settings, 'GIGYA_API_KEY', 'foo-bar')


