from .client import lastfm_request


'''
Sample response:
{
    "tag": {
        "name": "idm",
        "total": 266453,
        "reach": 39035,
        "wiki": {
            "summary": "IDM can refer both to intelligent dance music (aka Braindance) and industrial death metal. IDM is a popular name for an electronic music genre that emerged in the early 1990s at the end of the British rave era. The genre is influenced by a wide range of musical styles particularly electronic dance music (EDM) such as Detroit techno. Stylistically, IDM tends to rely upon individualistic experimentation rather than on a particular set of musical characteristics. <a href=\"http://www.last.fm/tag/idm\">Read more on Last.fm</a>.",
            "content": "IDM can refer both to intelligent dance music (aka Braindance) and industrial death metal. IDM is a popular name for an electronic music genre that emerged in the early 1990s at the end of the British rave era. The genre is influenced by a wide range of musical styles particularly electronic dance music (EDM) such as Detroit techno. Stylistically, IDM tends to rely upon individualistic experimentation rather than on a particular set of musical characteristics. The range of post-techno styles to emerge in the early 1990s were described variously as art techno, ambient techno, intelligent techno, and electronica. In America the latter term is now used by the music industry as a catchall to describe EDM and its many derivatives.\n\nThe term IDM is said to have originated in the United States in 1993 with the formation of the IDM list, an electronic mailing list originally charted for the discussion of music by (but not limited to) a number of prominent British artists, especially those appearing on a 1992 Warp Records compilation called Artificial Intelligence. The term is still seen by some as being peculiar to the U.S. but it is routinely used by music journalists, record labels, and fans on both sides of the Atlantic. <a href=\"http://www.last.fm/tag/idm\">Read more on Last.fm</a>. User-contributed text is available under the Creative Commons By-SA License; additional terms may apply."
        }
    }
}
'''
def get_info(tag):
    return lastfm_request("tag.getInfo", {"tag": tag})


'''
Sample response:
{
    "similartags": {
        "tag": [],
        "@attr": {
            "tag": "n/a"
        }
    }
}
NOTE: The response is almost always empty; avoid using this endpoint.
'''
def get_similar(tag):
    return lastfm_request("tag.getSimilar", {"tag": tag})


'''
Sample response:
{
    "albums": {
        "album": [
            {
                "name": "Richard D. James Album",
                "mbid": "16ca684d-53bc-4777-8129-6f779bf26ac9",
                "url": "https://www.last.fm/music/Aphex+Twin/Richard+D.+James+Album",
                "artist": {
                    "name": "Aphex Twin",
                    "mbid": "f22942a1-6f70-4f48-866e-238cb2308fbd",
                    "url": "https://www.last.fm/music/Aphex+Twin"
                },
                "image": [
                    {
                        "#text": "https://lastfm.freetls.fastly.net/i/u/34s/45bf620617914325c36163caf505c527.png",
                        "size": "small"
                    },
                    {
                        "#text": "https://lastfm.freetls.fastly.net/i/u/64s/45bf620617914325c36163caf505c527.png",
                        "size": "medium"
                    },
                    {
                        "#text": "https://lastfm.freetls.fastly.net/i/u/174s/45bf620617914325c36163caf505c527.png",
                        "size": "large"
                    },
                    {
                        "#text": "https://lastfm.freetls.fastly.net/i/u/300x300/45bf620617914325c36163caf505c527.png",
                        "size": "extralarge"
                    }
                ],
                "@attr": {
                    "rank": "1"
                }
            },
            {
                "name": "Tri Repetae",
                "mbid": "1683c0fb-6707-4234-99aa-3a71323e2779",
                "url": "https://www.last.fm/music/Autechre/Tri+Repetae",
                "artist": {
                    "name": "Autechre",
                    "mbid": "410c9baf-5469-44f6-9852-826524b80c61",
                    "url": "https://www.last.fm/music/Autechre"
                },
                "image": [
                    {
                        "#text": "https://lastfm.freetls.fastly.net/i/u/34s/62c1051bbfa76d491944a8b6a73db0ba.png",
                        "size": "small"
                    },
                    {
                        "#text": "https://lastfm.freetls.fastly.net/i/u/64s/62c1051bbfa76d491944a8b6a73db0ba.png",
                        "size": "medium"
                    },
                    {
                        "#text": "https://lastfm.freetls.fastly.net/i/u/174s/62c1051bbfa76d491944a8b6a73db0ba.png",
                        "size": "large"
                    },
                    {
                        "#text": "https://lastfm.freetls.fastly.net/i/u/300x300/62c1051bbfa76d491944a8b6a73db0ba.png",
                        "size": "extralarge"
                    }
                ],
                "@attr": {
                    "rank": "2"
                }
            }
        ],
        "@attr": {
            "tag": "idm",
            "page": "1",
            "perPage": "2",
            "totalPages": "3507",
            "total": "7013"
        }
    }
}
'''
def get_top_albums(tag, limit=None):
    params = {"tag": tag}
    if limit:
        params["limit"] = limit

    return lastfm_request("tag.getTopAlbums", params)


'''
Sample response:
{
    "topartists": {
        "artist": [
            {
                "name": "Wisp",
                "mbid": "4159ac30-ecce-43a6-b200-b48801968e30",
                "url": "https://www.last.fm/music/Wisp",
                "streamable": "0",
                "image": [
                    {
                        "#text": "https://lastfm.freetls.fastly.net/i/u/34s/2a96cbd8b46e442fc41c2b86b821562f.png",
                        "size": "small"
                    },
                    {
                        "#text": "https://lastfm.freetls.fastly.net/i/u/64s/2a96cbd8b46e442fc41c2b86b821562f.png",
                        "size": "medium"
                    },
                    {
                        "#text": "https://lastfm.freetls.fastly.net/i/u/174s/2a96cbd8b46e442fc41c2b86b821562f.png",
                        "size": "large"
                    },
                    {
                        "#text": "https://lastfm.freetls.fastly.net/i/u/300x300/2a96cbd8b46e442fc41c2b86b821562f.png",
                        "size": "extralarge"
                    },
                    {
                        "#text": "https://lastfm.freetls.fastly.net/i/u/300x300/2a96cbd8b46e442fc41c2b86b821562f.png",
                        "size": "mega"
                    }
                ],
                "@attr": {
                    "rank": "1"
                }
            },
            {
                "name": "Aphex Twin",
                "mbid": "f22942a1-6f70-4f48-866e-238cb2308fbd",
                "url": "https://www.last.fm/music/Aphex+Twin",
                "streamable": "0",
                "image": [
                    {
                        "#text": "https://lastfm.freetls.fastly.net/i/u/34s/2a96cbd8b46e442fc41c2b86b821562f.png",
                        "size": "small"
                    },
                    {
                        "#text": "https://lastfm.freetls.fastly.net/i/u/64s/2a96cbd8b46e442fc41c2b86b821562f.png",
                        "size": "medium"
                    },
                    {
                        "#text": "https://lastfm.freetls.fastly.net/i/u/174s/2a96cbd8b46e442fc41c2b86b821562f.png",
                        "size": "large"
                    },
                    {
                        "#text": "https://lastfm.freetls.fastly.net/i/u/300x300/2a96cbd8b46e442fc41c2b86b821562f.png",
                        "size": "extralarge"
                    },
                    {
                        "#text": "https://lastfm.freetls.fastly.net/i/u/300x300/2a96cbd8b46e442fc41c2b86b821562f.png",
                        "size": "mega"
                    }
                ],
                "@attr": {
                    "rank": "2"
                }
            }
        ],
        "@attr": {
            "tag": "idm",
            "page": "1",
            "perPage": "2",
            "totalPages": "7407",
            "total": "14814"
        }
    }
}
'''
def get_top_artists(tag, limit=None):
    params = {"tag": tag}
    if limit:
        params["limit"] = limit

    return lastfm_request("tag.getTopArtists", params)


'''
Sample response:
{
    "tracks": {
        "track": [
            {
                "name": "Alberto Balsalm",
                "duration": "108",
                "mbid": "89a75e8a-92d3-3997-9e3e-44c66c828221",
                "url": "https://www.last.fm/music/Aphex+Twin/_/Alberto+Balsalm",
                "streamable": {
                    "#text": "0",
                    "fulltrack": "0"
                },
                "artist": {
                    "name": "Aphex Twin",
                    "mbid": "f22942a1-6f70-4f48-866e-238cb2308fbd",
                    "url": "https://www.last.fm/music/Aphex+Twin"
                },
                "image": [
                    {
                        "#text": "https://lastfm.freetls.fastly.net/i/u/34s/2a96cbd8b46e442fc41c2b86b821562f.png",
                        "size": "small"
                    },
                    {
                        "#text": "https://lastfm.freetls.fastly.net/i/u/64s/2a96cbd8b46e442fc41c2b86b821562f.png",
                        "size": "medium"
                    },
                    {
                        "#text": "https://lastfm.freetls.fastly.net/i/u/174s/2a96cbd8b46e442fc41c2b86b821562f.png",
                        "size": "large"
                    },
                    {
                        "#text": "https://lastfm.freetls.fastly.net/i/u/300x300/2a96cbd8b46e442fc41c2b86b821562f.png",
                        "size": "extralarge"
                    }
                ],
                "@attr": {
                    "rank": "1"
                }
            },
            {
                "name": "IZ-US",
                "duration": "0",
                "mbid": "10324a48-3744-4ba3-b9a2-6dcc62e9c386",
                "url": "https://www.last.fm/music/Aphex+Twin/_/IZ-US",
                "streamable": {
                    "#text": "0",
                    "fulltrack": "0"
                },
                "artist": {
                    "name": "Aphex Twin",
                    "mbid": "f22942a1-6f70-4f48-866e-238cb2308fbd",
                    "url": "https://www.last.fm/music/Aphex+Twin"
                },
                "image": [
                    {
                        "#text": "https://lastfm.freetls.fastly.net/i/u/34s/2a96cbd8b46e442fc41c2b86b821562f.png",
                        "size": "small"
                    },
                    {
                        "#text": "https://lastfm.freetls.fastly.net/i/u/64s/2a96cbd8b46e442fc41c2b86b821562f.png",
                        "size": "medium"
                    },
                    {
                        "#text": "https://lastfm.freetls.fastly.net/i/u/174s/2a96cbd8b46e442fc41c2b86b821562f.png",
                        "size": "large"
                    },
                    {
                        "#text": "https://lastfm.freetls.fastly.net/i/u/300x300/2a96cbd8b46e442fc41c2b86b821562f.png",
                        "size": "extralarge"
                    }
                ],
                "@attr": {
                    "rank": "2"
                }
            }
        ],
        "@attr": {
            "tag": "idm",
            "page": "1",
            "perPage": "2",
            "totalPages": "18",
            "total": "35"
        }
    }
}
'''
def get_top_tracks(tag, limit=None):
    params = {"tag": tag}
    if limit:
        params["limit"] = limit

    return lastfm_request("tag.getTopTracks", params)
