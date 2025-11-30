from .client import lastfm_request

def get_top_artists(country, limit=None):
    params = {"country": country}
    if limit:
        params["limit"] = limit

    return lastfm_request("geo.getTopArtists", params)


def get_top_tracks(country, limit=None):
    params = {"country": country}
    if limit:
        params["limit"] = limit

    return lastfm_request("geo.getTopTracks", params)
