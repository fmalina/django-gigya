"""
GRequest class implementing calls to GIGYA REST API

method = "socialize.setStatus"
params = {"uid": "PUT-UID-HERE", "status": "I feel great"}
"""
from GSSDK import GSRequest, SigUtils
from django.conf import settings


class GigyaAuth:

    ERROR_CODE_VALIDATION = 400009
    ERROR_CODE_UNIQUE_IDENTIFIER_EXISTS = 400003
    ERROR_CODE_SUCCESS = 0

    def request(self, method, params):
        r = GSRequest(settings.GIGYA_API_KEY, settings.GIGYA_SECRET_KEY, method, params)
        r.setAPIDomain(settings.GIGYA_API_DOMAIN)
        response = r.send()

        if response.getErrorCode() != 0:  # response status NOT OK
            print(response.getErrorMessage())
            print(response.getLog())
        return response
