from GSSDK import GSRequest, SigUtils
from django.conf import settings

API_KEY = settings.GIGYA_API_KEY
SECRET_KEY = settings.GIGYA_SECRET_KEY

method = "socialize.setStatus"
params = {"uid": "PUT-UID-HERE", "status": "I feel great"}

request = GSRequest(API_KEY, SECRET_KEY, method, params)
request.setAPIDomain("eu1.gigya.com")
response = request.send()

if (response.getErrorCode()==0):
    # SUCCESS! response status = OK
    print "Success in setStatus operation."
else:
    # Error
    print "Got error on setStatus: " + response.getErrorMessage()
    # You may also log the response: response.getLog()
