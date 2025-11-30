from .client import lastfm_request

def get_info(tag):
    return lastfm_request("tag.getInfo", {"tag": tag})


def get_similar(tag):
    return lastfm_request("tag.getSimilar", {"tag": tag})


def get_top_albums(tag, limit=None):
    params = {"tag": tag}
    if limit:
        params["limit"] = limit

    return lastfm_request("tag.getTopAlbums", params)


def get_top_artists(tag, limit=None):
    params = {"tag": tag}
    if limit:
        params["limit"] = limit

    return lastfm_request("tag.getTopArtists", params)


def get_top_tracks(tag, limit=None):
    params = {"tag": tag}
    if limit:
        params["limit"] = limit

    return lastfm_request("tag.getTopTracks", params)
