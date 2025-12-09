from .client import lastfm_request


'''
Sample response (with username):
{
    "track": {
        "name": "Windowlicker",
        "mbid": "5011ada7-11c3-34cc-b544-9eafda54a2b0",
        "url": "https://www.last.fm/music/Aphex+Twin/_/Windowlicker",
        "duration": "233000",
        "streamable": {
            "#text": "0",
            "fulltrack": "0"
        },
        "listeners": "546026",
        "playcount": "4060185",
        "artist": {
            "name": "Aphex Twin",
            "mbid": "f22942a1-6f70-4f48-866e-238cb2308fbd",
            "url": "https://www.last.fm/music/Aphex+Twin"
        },
        "album": {
            "artist": "Aphex Twin",
            "title": "Windowlicker",
            "url": "https://www.last.fm/music/Aphex+Twin/Windowlicker",
            "image": [
                {
                    "#text": "https://lastfm.freetls.fastly.net/i/u/34s/5f7672bfc3b25879e26d6e588cc88534.png",
                    "size": "small"
                },
                {
                    "#text": "https://lastfm.freetls.fastly.net/i/u/64s/5f7672bfc3b25879e26d6e588cc88534.png",
                    "size": "medium"
                },
                {
                    "#text": "https://lastfm.freetls.fastly.net/i/u/174s/5f7672bfc3b25879e26d6e588cc88534.png",
                    "size": "large"
                },
                {
                    "#text": "https://lastfm.freetls.fastly.net/i/u/300x300/5f7672bfc3b25879e26d6e588cc88534.png",
                    "size": "extralarge"
                }
            ]
        },
        "userplaycount": "48",
        "userloved": "0",
        "toptags": {
            "tag": []
        },
        "wiki": {
            "published": "09 Jan 2010, 20:04",
            "summary": "Windowlicker is a song by electronic musician Aphex Twin, released on 22 March 1999 as a single by Warp Records. The artwork for the single was created by Chris Cunningham, with additional work by The Designers Republic. Cunningham also directed the song's music video, which was nominated for the Brit Award for Best British Video.\nThe song peaked at number 16 on the UK Singles Chart, and was later voted by fans as Warp Records' most popular song for its 2009 Warp20 compilation. <a href=\"http://www.last.fm/music/Aphex+Twin/_/Windowlicker\">Read more on Last.fm</a>.",
            "content": "Windowlicker is a song by electronic musician Aphex Twin, released on 22 March 1999 as a single by Warp Records. The artwork for the single was created by Chris Cunningham, with additional work by The Designers Republic. Cunningham also directed the song's music video, which was nominated for the Brit Award for Best British Video.\nThe song peaked at number 16 on the UK Singles Chart, and was later voted by fans as Warp Records' most popular song for its 2009 Warp20 compilation. Pitchfork included the song at number 12 on their list Top 200 Tracks of the 90s.\n\n\"Windowlicker\" focuses stylistically on \"eerie lounge-porn music\" and features rapid breakbeat drum programming and heavily manipulated vocals. According to CMJ New Music, the track's \"electro drum kicks, warped vocal samples and sleazy, erotic ambiance connote images and emotions alien to James's previous compositions.\" Gasps and moans reminiscent of sexual vocal tones \"glide in and out of the production\"; some fans speculate that the vocals are James's own treated voice. The track consists of various sections, including a drum'n'bass intro, a \"gooey middle section\", and an abrasive noise ending, as well featuring a consistent melodic element throughout. DJ Mag labeled its sound an \"uncompromising cyborg R&B,\" while Fact labeled it \"R&B and hip-hop written in the language of glitches and breakbeats.\"\nIn 2012, Pitchfork stated that the track's futuristic elements presaged various musical developments, including \"Flying Lotus' digital deconstruction, James Blake's bent vocals, [and] the wobble and knock of dubstep\". Similarly, Stereogum stated that \"the song's mix of unpredictable syncopation, digital-dub alien transformations, errant noises, and bursts of melody would serve as a starting block for much of today's electronic music\" it took a big role playing in the movie \"climax\" by gaspar noe (2018) <a href=\"http://www.last.fm/music/Aphex+Twin/_/Windowlicker\">Read more on Last.fm</a>. User-contributed text is available under the Creative Commons By-SA License; additional terms may apply."
        }
    }
}
'''
'''
Sample response (without username):
{
    "track": {
        "name": "Windowlicker",
        "mbid": "5011ada7-11c3-34cc-b544-9eafda54a2b0",
        "url": "https://www.last.fm/music/Aphex+Twin/_/Windowlicker",
        "duration": "233000",
        "streamable": {
            "#text": "0",
            "fulltrack": "0"
        },
        "listeners": "546026",
        "playcount": "4060185",
        "artist": {
            "name": "Aphex Twin",
            "mbid": "f22942a1-6f70-4f48-866e-238cb2308fbd",
            "url": "https://www.last.fm/music/Aphex+Twin"
        },
        "album": {
            "artist": "Aphex Twin",
            "title": "Windowlicker",
            "url": "https://www.last.fm/music/Aphex+Twin/Windowlicker",
            "image": [
                {
                    "#text": "https://lastfm.freetls.fastly.net/i/u/34s/5f7672bfc3b25879e26d6e588cc88534.png",
                    "size": "small"
                },
                {
                    "#text": "https://lastfm.freetls.fastly.net/i/u/64s/5f7672bfc3b25879e26d6e588cc88534.png",
                    "size": "medium"
                },
                {
                    "#text": "https://lastfm.freetls.fastly.net/i/u/174s/5f7672bfc3b25879e26d6e588cc88534.png",
                    "size": "large"
                },
                {
                    "#text": "https://lastfm.freetls.fastly.net/i/u/300x300/5f7672bfc3b25879e26d6e588cc88534.png",
                    "size": "extralarge"
                }
            ]
        },
        "toptags": {
            "tag": []
        },
        "wiki": {
            "published": "09 Jan 2010, 20:04",
            "summary": "Windowlicker is a song by electronic musician Aphex Twin, released on 22 March 1999 as a single by Warp Records. The artwork for the single was created by Chris Cunningham, with additional work by The Designers Republic. Cunningham also directed the song's music video, which was nominated for the Brit Award for Best British Video.\nThe song peaked at number 16 on the UK Singles Chart, and was later voted by fans as Warp Records' most popular song for its 2009 Warp20 compilation. <a href=\"http://www.last.fm/music/Aphex+Twin/_/Windowlicker\">Read more on Last.fm</a>.",
            "content": "Windowlicker is a song by electronic musician Aphex Twin, released on 22 March 1999 as a single by Warp Records. The artwork for the single was created by Chris Cunningham, with additional work by The Designers Republic. Cunningham also directed the song's music video, which was nominated for the Brit Award for Best British Video.\nThe song peaked at number 16 on the UK Singles Chart, and was later voted by fans as Warp Records' most popular song for its 2009 Warp20 compilation. Pitchfork included the song at number 12 on their list Top 200 Tracks of the 90s.\n\n\"Windowlicker\" focuses stylistically on \"eerie lounge-porn music\" and features rapid breakbeat drum programming and heavily manipulated vocals. According to CMJ New Music, the track's \"electro drum kicks, warped vocal samples and sleazy, erotic ambiance connote images and emotions alien to James's previous compositions.\" Gasps and moans reminiscent of sexual vocal tones \"glide in and out of the production\"; some fans speculate that the vocals are James's own treated voice. The track consists of various sections, including a drum'n'bass intro, a \"gooey middle section\", and an abrasive noise ending, as well featuring a consistent melodic element throughout. DJ Mag labeled its sound an \"uncompromising cyborg R&B,\" while Fact labeled it \"R&B and hip-hop written in the language of glitches and breakbeats.\"\nIn 2012, Pitchfork stated that the track's futuristic elements presaged various musical developments, including \"Flying Lotus' digital deconstruction, James Blake's bent vocals, [and] the wobble and knock of dubstep\". Similarly, Stereogum stated that \"the song's mix of unpredictable syncopation, digital-dub alien transformations, errant noises, and bursts of melody would serve as a starting block for much of today's electronic music\" it took a big role playing in the movie \"climax\" by gaspar noe (2018) <a href=\"http://www.last.fm/music/Aphex+Twin/_/Windowlicker\">Read more on Last.fm</a>. User-contributed text is available under the Creative Commons By-SA License; additional terms may apply."
        }
    }
}
'''
def get_info(artist, track, username=None):
    params = {
        "artist": artist,
        "track": track
    }
    if username:
        params["username"] = username

    return lastfm_request("track.getInfo", params)


'''
Sample response:
{
    "similartracks": {
        "track": [
            {
                "name": "Nannou",
                "playcount": 632960,
                "mbid": "00e7e5c1-63af-3deb-9be0-602d4c230558",
                "match": 1.0,
                "url": "https://www.last.fm/music/Aphex+Twin/_/Nannou",
                "streamable": {
                    "#text": "0",
                    "fulltrack": "0"
                },
                "duration": 253,
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
                    },
                    {
                        "#text": "https://lastfm.freetls.fastly.net/i/u/300x300/2a96cbd8b46e442fc41c2b86b821562f.png",
                        "size": "mega"
                    },
                    {
                        "#text": "https://lastfm.freetls.fastly.net/i/u/300x300/2a96cbd8b46e442fc41c2b86b821562f.png",
                        "size": ""
                    }
                ]
            },
            {
                "name": "4",
                "playcount": 2635904,
                "mbid": "0d97b779-eb17-3c74-8d8a-dec13e395c32",
                "match": 0.911704,
                "url": "https://www.last.fm/music/Aphex+Twin/_/4",
                "streamable": {
                    "#text": "0",
                    "fulltrack": "0"
                },
                "duration": 217,
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
                    },
                    {
                        "#text": "https://lastfm.freetls.fastly.net/i/u/300x300/2a96cbd8b46e442fc41c2b86b821562f.png",
                        "size": "mega"
                    },
                    {
                        "#text": "https://lastfm.freetls.fastly.net/i/u/300x300/2a96cbd8b46e442fc41c2b86b821562f.png",
                        "size": ""
                    }
                ]
            }
        ],
        "@attr": {
            "artist": "Aphex Twin",
            "track": "Windowlicker"
        }
    }
}
'''
def get_similar(artist, track, limit=None):
    params = {
        "artist": artist,
        "track": track
    }
    if limit:
        params["limit"] = limit

    return lastfm_request("track.getSimilar", params)


'''
Sample response:
{
    "toptags": {
        "tag": [],
        "@attr": {
            "artist": "Aphex Twin",
            "track": "Windowlicker"
        }
    }
}
NOTE: The response is almost always empty; avoid using this endpoint.
'''
def get_top_tags(artist, track):
    return lastfm_request("track.getTopTags", {
        "artist": artist,
        "track": track
    })
