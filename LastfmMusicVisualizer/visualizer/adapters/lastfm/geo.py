from .client import lastfm_request


'''
Sample response:
{
    "topartists": {
        "artist": [
            {
                "name": "Tyler, The Creator",
                "listeners": "267751",
                "mbid": "f6beac20-5dfe-4d1f-ae02-0b0a740aafd6",
                "url": "https://www.last.fm/music/Tyler,+The+Creator",
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
                "name": "Kendrick Lamar",
                "listeners": "253944",
                "mbid": "381086ea-f511-4aba-bdf9-71c753dc5077",
                "url": "https://www.last.fm/music/Kendrick+Lamar",
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
            "country": "United States",
            "page": "1",
            "perPage": "2",
            "totalPages": "1133",
            "total": "2265"
        }
    }
}
'''
def get_top_artists(country, limit=None):
    params = {"country": country}
    if limit:
        params["limit"] = limit

    return lastfm_request("geo.getTopArtists", params)


'''
Sample response:
{
    "tracks": {
        "track": [
            {
                "name": "Sienna",
                "duration": "224",
                "listeners": "66700",
                "mbid": "f3db7473-3a61-4053-a7ce-a8fe29dbe5fa",
                "url": "https://www.last.fm/music/The+Mar%C3%ADas/_/Sienna",
                "streamable": {
                    "#text": "0",
                    "fulltrack": "0"
                },
                "artist": {
                    "name": "The Mar\u00edas",
                    "mbid": "7a3970c9-ecd8-4eee-a267-4d8c77d97ff3",
                    "url": "https://www.last.fm/music/The+Mar%C3%ADas"
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
                    "rank": "0"
                }
            },
            {
                "name": "No One Noticed",
                "duration": "236",
                "listeners": "65145",
                "mbid": "d13a634b-9f69-4256-9415-b7e95aac101d",
                "url": "https://www.last.fm/music/The+Mar%C3%ADas/_/No+One+Noticed",
                "streamable": {
                    "#text": "0",
                    "fulltrack": "0"
                },
                "artist": {
                    "name": "The Mar\u00edas",
                    "mbid": "7a3970c9-ecd8-4eee-a267-4d8c77d97ff3",
                    "url": "https://www.last.fm/music/The+Mar%C3%ADas"
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
            }
        ],
        "@attr": {
            "country": "United States",
            "page": "1",
            "perPage": "2",
            "totalPages": "5000",
            "total": "10000"
        }
    }
}
'''
def get_top_tracks(country, limit=None):
    params = {"country": country}
    if limit:
        params["limit"] = limit

    return lastfm_request("geo.getTopTracks", params)
