import re
import requests
from .client import lastfm_request

USERNAME_REGEX = re.compile(r'^[A-Za-z0-9_\-]+$')

def validate_lastfm_username(username):
    # Check allowed characters
    if not USERNAME_REGEX.match(username):
        return False, "Invalid username format."

    # Check existence via Last.fm API
    try:
        response = lastfm_request("user.getInfo", {"user": username})

        # If user doesn't exist, Last.fm returns an "error" key
        data = response.json()

    except requests.exceptions.HTTPError:
        # Last.fm returns 404 for nonexistent users
        return False, "That Last.fm username does not exist."

    except requests.exceptions.RequestException:
        # Network timeout, DNS, etc.
        return False, "Could not connect to Last.fm. Please try again."

    # Last.fm still sometimes returns a 200 response even if the user doesn't exist
    if isinstance(data, dict) and 'error' in data:
        return False, "That Last.fm username does not exist."

    return True, None