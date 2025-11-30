from .client import lastfm_request

def get_info(artist, username=None):
    params = {"artist": artist}
    if username:
        params["username"] = username

    return lastfm_request("artist.getInfo", params)


def get_similar(artist, limit=None):
    params = {"artist": artist}
    if limit:
        params["limit"] = limit

    return lastfm_request("artist.getSimilar", params)


def get_top_albums(artist, limit=None):
    params = {"artist": artist}
    if limit:
        params["limit"] = limit

    return lastfm_request("artist.getTopAlbums", params)


def get_top_tags(artist):
    return lastfm_request("artist.getTopTags", {"artist": artist})


def get_top_tracks(artist, limit=None):
    params = {"artist": artist}
    if limit:
        params["limit"] = limit

    return lastfm_request("artist.getTopTracks", params)
