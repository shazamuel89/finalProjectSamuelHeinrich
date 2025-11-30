from .client import lastfm_request

def get_info(user):
    return lastfm_request("user.getInfo", {"user": user})


def get_recent_tracks(user, limit=None, page=None, from_ts=None, to_ts=None, extended=None):
    params = {"user": user}

    if limit: params["limit"] = limit
    if page: params["page"] = page
    if from_ts: params["from"] = from_ts
    if to_ts: params["to"] = to_ts
    if extended: params["extended"] = extended  # 1/0

    return lastfm_request("user.getRecentTracks", params)


def get_top_albums(user, period=None, limit=None, page=None):
    params = {"user": user}

    if period: params["period"] = period
    if limit: params["limit"] = limit
    if page: params["page"] = page

    return lastfm_request("user.getTopAlbums", params)


def get_top_artists(user, period=None, limit=None, page=None):
    params = {"user": user}

    if period: params["period"] = period
    if limit: params["limit"] = limit
    if page: params["page"] = page

    return lastfm_request("user.getTopArtists", params)


def get_top_tracks(user, period=None, limit=None, page=None):
    params = {"user": user}

    if period: params["period"] = period
    if limit: params["limit"] = limit
    if page: params["page"] = page

    return lastfm_request("user.getTopTracks", params)


def get_weekly_album_chart(user, limit=None, from_ts=None, to_ts=None):
    params = {"user": user}

    if limit: params["limit"] = limit
    if from_ts: params["from"] = from_ts
    if to_ts: params["to"] = to_ts

    return lastfm_request("user.getWeeklyAlbumChart", params)


def get_weekly_artist_chart(user, limit=None, from_ts=None, to_ts=None):
    params = {"user": user}

    if limit: params["limit"] = limit
    if from_ts: params["from"] = from_ts
    if to_ts: params["to"] = to_ts

    return lastfm_request("user.getWeeklyArtistChart", params)


def get_weekly_chart_list(user):
    return lastfm_request("user.getWeeklyChartList", {"user": user})


def get_weekly_track_chart(user, limit=None, from_ts=None, to_ts=None):
    params = {"user": user}

    if limit: params["limit"] = limit
    if from_ts: params["from"] = from_ts
    if to_ts: params["to"] = to_ts

    return lastfm_request("user.getWeeklyTrackChart", params)
