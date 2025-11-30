import requests
from django.conf import settings

api_key = settings.LASTFM_API_KEY
api_base = settings.LASTFM_API_BASE

def lastfm_request(method, params):
    payload = {
        "method": method,
        "api_key": api_key,
        "format": "json",
        **params
    }
    response = requests.get(api_base, params=payload)
    response.raise_for_status()
    return response.json()
