from .client import lastfm_request

def get_info(artist, album, username=None):
    params = {
        "artist": artist,
        "album": album
    }
    if username:
        params["username"] = username

    return lastfm_request("album.getInfo", params)


def get_top_tags(artist, album):
    return lastfm_request("album.getTopTags", {
        "artist": artist,
        "album": album
    })
