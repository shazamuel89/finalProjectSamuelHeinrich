from .client import lastfm_request

def get_info(artist, track, username=None):
    params = {
        "artist": artist,
        "track": track
    }
    if username:
        params["username"] = username

    return lastfm_request("track.getInfo", params)


def get_similar(artist, track, limit=None):
    params = {
        "artist": artist,
        "track": track
    }
    if limit:
        params["limit"] = limit

    return lastfm_request("track.getSimilar", params)


def get_top_tags(artist, track):
    return lastfm_request("track.getTopTags", {
        "artist": artist,
        "track": track
    })
