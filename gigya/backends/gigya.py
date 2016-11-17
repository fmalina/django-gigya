"""
GRequest class implementing calls to GIGYA REST API

method = "socialize.setStatus"
params = {"uid": "PUT-UID-HERE", "status": "I feel great"}
"""
from GSSDK import GSRequest, SigUtils
from django.conf import settings


class GRequest():
    def request(self, method, params):

        r = GSRequest(settings.GIGYA_API_KEY, settings.GIGYA_SECRET_KEY, method, params)
        r.setAPIDomain("eu1.gigya.com")
        response = r.send()

        if response.getErrorCode() != 0:  # response status NOT OK
            print("Error")
            return (response.getErrorMessage(),
                    response.getLog())
        return response
