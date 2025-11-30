import requests
from django.conf import settings

API_KEY = settings.LASTFM_API_KEY
BASE = settings.LASTFM_API_BASE

def lastfm_request(method, params):
    """
    Helper function that calls the Last.fm API and returns parsed JSON.
    """
    payload = {
        "method": method,
        "api_key": API_KEY,
        "format": "json",
    }
    payload.update(params)

    response = requests.get(BASE, params=payload)
    response.raise_for_status()
    return response.json()


def fetch_user_overview(username):
    """
    Fetch basic profile + total scrobbles.
    """
    data = lastfm_request("user.getInfo", {"user": username})

    user = data.get("user", {})

    return {
        "display_name": user.get("name"),
        "profile_url": user.get("url"),
        "avatar_url": user.get("image", [{}])[-1].get("#text", None),
        "total_scrobbles": int(user.get("playcount", 0)),
        "registered_date": user.get("registered", {}).get("#text"),
    }


def fetch_top_artists(username, limit=10):
    data = lastfm_request("user.getTopArtists", {"user": username, "limit": limit})
    return data.get("topartists", {}).get("artist", [])


def fetch_top_albums(username, limit=10):
    data = lastfm_request("user.getTopAlbums", {"user": username, "limit": limit})
    return data.get("topalbums", {}).get("album", [])


def fetch_top_tracks(username, limit=10):
    data = lastfm_request("user.getTopTracks", {"user": username, "limit": limit})
    return data.get("toptracks", {}).get("track", [])


def fetch_recent_tracks(username, limit=20):
    data = lastfm_request("user.getRecentTracks", {"user": username, "limit": limit})
    return data.get("recenttracks", {}).get("track", [])