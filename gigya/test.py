from GSSDK import GSRequest
from django.conf import settings

API_KEY = settings.GIGYA_API_KEY
SECRET_KEY = settings.GIGYA_SECRET_KEY

method = ''
params = {}

request = GSRequest(API_KEY, SECRET_KEY, method, params)
request.setAPIDomain("eu1.gigya.com")
