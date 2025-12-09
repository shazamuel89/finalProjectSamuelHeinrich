from .client import lastfm_request


'''
Sample response (with username):
{
    "album": {
        "artist": "Aphex Twin",
        "mbid": "0a25ae72-8a79-37f4-a697-591f4364e0ab",
        "tags": {
            "tag": [
                {
                    "url": "https://www.last.fm/tag/electronic",
                    "name": "electronic"
                },
                {
                    "url": "https://www.last.fm/tag/idm",
                    "name": "idm"
                },
                {
                    "url": "https://www.last.fm/tag/ambient",
                    "name": "ambient"
                },
                {
                    "url": "https://www.last.fm/tag/experimental",
                    "name": "experimental"
                },
                {
                    "url": "https://www.last.fm/tag/electronica",
                    "name": "electronica"
                }
            ]
        },
        "name": "Windowlicker",
        "userplaycount": 142,
        "image": [
            {
                "size": "small",
                "#text": "https://lastfm.freetls.fastly.net/i/u/34s/5f7672bfc3b25879e26d6e588cc88534.jpg"
            },
            {
                "size": "medium",
                "#text": "https://lastfm.freetls.fastly.net/i/u/64s/5f7672bfc3b25879e26d6e588cc88534.jpg"
            },
            {
                "size": "large",
                "#text": "https://lastfm.freetls.fastly.net/i/u/174s/5f7672bfc3b25879e26d6e588cc88534.jpg"
            },
            {
                "size": "extralarge",
                "#text": "https://lastfm.freetls.fastly.net/i/u/300x300/5f7672bfc3b25879e26d6e588cc88534.jpg"
            },
            {
                "size": "mega",
                "#text": "https://lastfm.freetls.fastly.net/i/u/300x300/5f7672bfc3b25879e26d6e588cc88534.jpg"
            },
            {
                "size": "",
                "#text": "https://lastfm.freetls.fastly.net/i/u/300x300/5f7672bfc3b25879e26d6e588cc88534.jpg"
            }
        ],
        "tracks": {
            "track": [
                {
                    "streamable": {
                        "fulltrack": "0",
                        "#text": "0"
                    },
                    "duration": 233,
                    "url": "https://www.last.fm/music/Aphex+Twin/Windowlicker/Windowlicker",
                    "name": "Windowlicker",
                    "@attr": {
                        "rank": 1
                    },
                    "artist": {
                        "url": "https://www.last.fm/music/Aphex+Twin",
                        "name": "Aphex Twin",
                        "mbid": "f22942a1-6f70-4f48-866e-238cb2308fbd"
                    }
                },
                {
                    "streamable": {
                        "fulltrack": "0",
                        "#text": "0"
                    },
                    "duration": 347,
                    "url": "https://www.last.fm/music/Aphex+Twin/Windowlicker/Formula",
                    "name": "Formula",
                    "@attr": {
                        "rank": 2
                    },
                    "artist": {
                        "url": "https://www.last.fm/music/Aphex+Twin",
                        "name": "Aphex Twin",
                        "mbid": "f22942a1-6f70-4f48-866e-238cb2308fbd"
                    }
                },
                {
                    "streamable": {
                        "fulltrack": "0",
                        "#text": "0"
                    },
                    "duration": 253,
                    "url": "https://www.last.fm/music/Aphex+Twin/Windowlicker/Nannou",
                    "name": "Nannou",
                    "@attr": {
                        "rank": 3
                    },
                    "artist": {
                        "url": "https://www.last.fm/music/Aphex+Twin",
                        "name": "Aphex Twin",
                        "mbid": "f22942a1-6f70-4f48-866e-238cb2308fbd"
                    }
                }
            ]
        },
        "listeners": "475092",
        "playcount": "3943785",
        "url": "https://www.last.fm/music/Aphex+Twin/Windowlicker",
        "wiki": {
            "published": "10 Oct 2022, 18:33",
            "summary": "Windowlicker is a song by electronic musician Aphex Twin, released on 22 March 1999 as a single by Warp Records. The artwork for the single was created by Chris Cunningham, with additional work by The Designers Republic. Cunningham also directed the song's music video, which was nominated for the Brit Award for Best British Video. The song peaked at number 16 on the UK Singles Chart, and was later voted by fans as Warp Records' most popular song for its 2009 Warp20 compilation. Pitchfork included the song at number 12 on their list Top 200 Tracks of the 90s. \"Windowlicker\" <a href=\"https://www.last.fm/music/Aphex+Twin/Windowlicker\">Read more on Last.fm</a>.",
            "content": "Windowlicker is a song by electronic musician Aphex Twin, released on 22 March 1999 as a single by Warp Records. The artwork for the single was created by Chris Cunningham, with additional work by The Designers Republic. Cunningham also directed the song's music video, which was nominated for the Brit Award for Best British Video.\nThe song peaked at number 16 on the UK Singles Chart, and was later voted by fans as Warp Records' most popular song for its 2009 Warp20 compilation. Pitchfork included the song at number 12 on their list Top 200 Tracks of the 90s.\n\n\"Windowlicker\" focuses stylistically on \"eerie lounge-porn music\" and features rapid breakbeat drum programming and heavily manipulated vocals. According to CMJ New Music, the track's \"electro drum kicks, warped vocal samples and sleazy, erotic ambiance connote images and emotions alien to James's previous compositions.\" Gasps and moans reminiscent of sexual vocal tones \"glide in and out of the production\"; some fans speculate that the vocals are James's own treated voice. The track consists of various sections, including a drum'n'bass intro, a \"gooey middle section\", and an abrasive noise ending, as well featuring a consistent melodic element throughout. DJ Mag labeled its sound an \"uncompromising cyborg R&B,\" while Fact labeled it \"R&B and hip-hop written in the language of glitches and breakbeats.\"\nIn 2012, Pitchfork stated that the track's futuristic elements presaged various musical developments, including \"Flying Lotus' digital deconstruction, James Blake's bent vocals,  the wobble and knock of dubstep\". Similarly, Stereogum stated that \"the song's mix of unpredictable syncopation, digital-dub alien transformations, errant noises, and bursts of melody would serve as a starting block for much of today's electronic music\". <a href=\"https://www.last.fm/music/Aphex+Twin/Windowlicker\">Read more on Last.fm</a>. User-contributed text is available under the Creative Commons By-SA License; additional terms may apply."
        }
    }
}
'''
'''
Sample response (without username):
{
    "album": {
        "artist": "Aphex Twin",
        "mbid": "0a25ae72-8a79-37f4-a697-591f4364e0ab",
        "tags": {
            "tag": [
                {
                    "url": "https://www.last.fm/tag/electronic",
                    "name": "electronic"
                },
                {
                    "url": "https://www.last.fm/tag/idm",
                    "name": "idm"
                },
                {
                    "url": "https://www.last.fm/tag/ambient",
                    "name": "ambient"
                },
                {
                    "url": "https://www.last.fm/tag/experimental",
                    "name": "experimental"
                },
                {
                    "url": "https://www.last.fm/tag/electronica",
                    "name": "electronica"
                }
            ]
        },
        "playcount": "3943785",
        "image": [
            {
                "size": "small",
                "#text": "https://lastfm.freetls.fastly.net/i/u/34s/5f7672bfc3b25879e26d6e588cc88534.jpg"
            },
            {
                "size": "medium",
                "#text": "https://lastfm.freetls.fastly.net/i/u/64s/5f7672bfc3b25879e26d6e588cc88534.jpg"
            },
            {
                "size": "large",
                "#text": "https://lastfm.freetls.fastly.net/i/u/174s/5f7672bfc3b25879e26d6e588cc88534.jpg"
            },
            {
                "size": "extralarge",
                "#text": "https://lastfm.freetls.fastly.net/i/u/300x300/5f7672bfc3b25879e26d6e588cc88534.jpg"
            },
            {
                "size": "mega",
                "#text": "https://lastfm.freetls.fastly.net/i/u/300x300/5f7672bfc3b25879e26d6e588cc88534.jpg"
            },
            {
                "size": "",
                "#text": "https://lastfm.freetls.fastly.net/i/u/300x300/5f7672bfc3b25879e26d6e588cc88534.jpg"
            }
        ],
        "tracks": {
            "track": [
                {
                    "streamable": {
                        "fulltrack": "0",
                        "#text": "0"
                    },
                    "duration": 233,
                    "url": "https://www.last.fm/music/Aphex+Twin/Windowlicker/Windowlicker",
                    "name": "Windowlicker",
                    "@attr": {
                        "rank": 1
                    },
                    "artist": {
                        "url": "https://www.last.fm/music/Aphex+Twin",
                        "name": "Aphex Twin",
                        "mbid": "f22942a1-6f70-4f48-866e-238cb2308fbd"
                    }
                },
                {
                    "streamable": {
                        "fulltrack": "0",
                        "#text": "0"
                    },
                    "duration": 347,
                    "url": "https://www.last.fm/music/Aphex+Twin/Windowlicker/Formula",
                    "name": "Formula",
                    "@attr": {
                        "rank": 2
                    },
                    "artist": {
                        "url": "https://www.last.fm/music/Aphex+Twin",
                        "name": "Aphex Twin",
                        "mbid": "f22942a1-6f70-4f48-866e-238cb2308fbd"
                    }
                },
                {
                    "streamable": {
                        "fulltrack": "0",
                        "#text": "0"
                    },
                    "duration": 253,
                    "url": "https://www.last.fm/music/Aphex+Twin/Windowlicker/Nannou",
                    "name": "Nannou",
                    "@attr": {
                        "rank": 3
                    },
                    "artist": {
                        "url": "https://www.last.fm/music/Aphex+Twin",
                        "name": "Aphex Twin",
                        "mbid": "f22942a1-6f70-4f48-866e-238cb2308fbd"
                    }
                }
            ]
        },
        "url": "https://www.last.fm/music/Aphex+Twin/Windowlicker",
        "name": "Windowlicker",
        "listeners": "475092",
        "wiki": {
            "published": "10 Oct 2022, 18:33",
            "summary": "Windowlicker is a song by electronic musician Aphex Twin, released on 22 March 1999 as a single by Warp Records. The artwork for the single was created by Chris Cunningham, with additional work by The Designers Republic. Cunningham also directed the song's music video, which was nominated for the Brit Award for Best British Video. The song peaked at number 16 on the UK Singles Chart, and was later voted by fans as Warp Records' most popular song for its 2009 Warp20 compilation. Pitchfork included the song at number 12 on their list Top 200 Tracks of the 90s. \"Windowlicker\" <a href=\"https://www.last.fm/music/Aphex+Twin/Windowlicker\">Read more on Last.fm</a>.",
            "content": "Windowlicker is a song by electronic musician Aphex Twin, released on 22 March 1999 as a single by Warp Records. The artwork for the single was created by Chris Cunningham, with additional work by The Designers Republic. Cunningham also directed the song's music video, which was nominated for the Brit Award for Best British Video.\nThe song peaked at number 16 on the UK Singles Chart, and was later voted by fans as Warp Records' most popular song for its 2009 Warp20 compilation. Pitchfork included the song at number 12 on their list Top 200 Tracks of the 90s.\n\n\"Windowlicker\" focuses stylistically on \"eerie lounge-porn music\" and features rapid breakbeat drum programming and heavily manipulated vocals. According to CMJ New Music, the track's \"electro drum kicks, warped vocal samples and sleazy, erotic ambiance connote images and emotions alien to James's previous compositions.\" Gasps and moans reminiscent of sexual vocal tones \"glide in and out of the production\"; some fans speculate that the vocals are James's own treated voice. The track consists of various sections, including a drum'n'bass intro, a \"gooey middle section\", and an abrasive noise ending, as well featuring a consistent melodic element throughout. DJ Mag labeled its sound an \"uncompromising cyborg R&B,\" while Fact labeled it \"R&B and hip-hop written in the language of glitches and breakbeats.\"\nIn 2012, Pitchfork stated that the track's futuristic elements presaged various musical developments, including \"Flying Lotus' digital deconstruction, James Blake's bent vocals,  the wobble and knock of dubstep\". Similarly, Stereogum stated that \"the song's mix of unpredictable syncopation, digital-dub alien transformations, errant noises, and bursts of melody would serve as a starting block for much of today's electronic music\". <a href=\"https://www.last.fm/music/Aphex+Twin/Windowlicker\">Read more on Last.fm</a>. User-contributed text is available under the Creative Commons By-SA License; additional terms may apply."
        }
    }
}
'''
def get_info(artist, album, username=None):
    params = {
        "artist": artist,
        "album": album
    }
    if username:
        params["username"] = username

    return lastfm_request("album.getInfo", params)


'''
Sample response:
{
    "toptags": {
        "tag": [
            {
                "count": 100,
                "name": "idm",
                "url": "https://www.last.fm/tag/idm"
            },
            {
                "count": 63,
                "name": "electronic",
                "url": "https://www.last.fm/tag/electronic"
            },
            {
                "count": 33,
                "name": "1999",
                "url": "https://www.last.fm/tag/1999"
            },
            {
                "count": 13,
                "name": "experimental",
                "url": "https://www.last.fm/tag/experimental"
            },
            {
                "count": 5,
                "name": "glitch",
                "url": "https://www.last.fm/tag/glitch"
            },
            {
                "count": 5,
                "name": "Playful",
                "url": "https://www.last.fm/tag/Playful"
            },
            {
                "count": 2,
                "name": "instrumental",
                "url": "https://www.last.fm/tag/instrumental"
            },
            {
                "count": 1,
                "name": "electronica",
                "url": "https://www.last.fm/tag/electronica"
            },
            {
                "count": 1,
                "name": "techno",
                "url": "https://www.last.fm/tag/techno"
            },
            {
                "count": 1,
                "name": "quirky",
                "url": "https://www.last.fm/tag/quirky"
            }
        ],
        "@attr": {
            "artist": "Aphex Twin",
            "album": "Windowlicker"
        }
    }
}
'''
def get_top_tags(artist, album):
    return lastfm_request("album.getTopTags", {
        "artist": artist,
        "album": album
    })
