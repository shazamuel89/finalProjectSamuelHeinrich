from .client import lastfm_request


'''
Sample response (with username):
{
    "artist": {
        "name": "Aphex Twin",
        "mbid": "f22942a1-6f70-4f48-866e-238cb2308fbd",
        "url": "https://www.last.fm/music/Aphex+Twin",
        "image": [
            {
                "#text": "https://lastfm.freetls.fastly.net/i/u/34s/8d1a1fda90b7e2cf43da7d33797a2a6e.jpg",
                "size": "small"
            },
            {
                "#text": "https://lastfm.freetls.fastly.net/i/u/64s/8d1a1fda90b7e2cf43da7d33797a2a6e.jpg",
                "size": "medium"
            },
            {
                "#text": "https://lastfm.freetls.fastly.net/i/u/174s/8d1a1fda90b7e2cf43da7d33797a2a6e.jpg",
                "size": "large"
            },
            {
                "#text": "https://lastfm.freetls.fastly.net/i/u/300x300/8d1a1fda90b7e2cf43da7d33797a2a6e.jpg",
                "size": "extralarge"
            },
            {
                "#text": "https://lastfm.freetls.fastly.net/i/u/300x300/8d1a1fda90b7e2cf43da7d33797a2a6e.jpg",
                "size": "mega"
            },
            {
                "#text": "https://lastfm.freetls.fastly.net/i/u/300x300/8d1a1fda90b7e2cf43da7d33797a2a6e.jpg",
                "size": ""
            }
        ],
        "streamable": "0",
        "ontour": "0",
        "stats": {
            "listeners": "2930282",
            "playcount": "212148914",
            "userplaycount": "3338"
        },
        "similar": {
            "artist": [
                {
                    "name": "AFX",
                    "url": "https://www.last.fm/music/AFX",
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
                    "name": "Polygon Window",
                    "url": "https://www.last.fm/music/Polygon+Window",
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
                    "name": "Squarepusher",
                    "url": "https://www.last.fm/music/Squarepusher",
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
                    "name": "Boards of Canada",
                    "url": "https://www.last.fm/music/Boards+of+Canada",
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
                    "name": "Autechre",
                    "url": "https://www.last.fm/music/Autechre",
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
            ]
        },
        "tags": {
            "tag": [
                {
                    "name": "electronic",
                    "url": "https://www.last.fm/tag/electronic"
                },
                {
                    "name": "idm",
                    "url": "https://www.last.fm/tag/idm"
                },
                {
                    "name": "ambient",
                    "url": "https://www.last.fm/tag/ambient"
                },
                {
                    "name": "experimental",
                    "url": "https://www.last.fm/tag/experimental"
                },
                {
                    "name": "electronica",
                    "url": "https://www.last.fm/tag/electronica"
                }
            ]
        },
        "bio": {
            "links": {
                "link": {
                    "#text": "",
                    "rel": "original",
                    "href": "https://last.fm/music/Aphex+Twin/+wiki"
                }
            },
            "published": "02 Feb 2006, 16:17",
            "summary": "Richard David James (born 18 August 1971), known professionally as Aphex Twin, is a British musician, composer, and DJ who has been active in electronic music since 1988. His work incorporates a variety of styles, including techno, ambient, acid, and jungle. He is often associated with the intelligent dance music (IDM) genre. Several publications such as Mixmag, The New York Times, NME, Fact, Clash, and The Guardian have recognized him as an influential figure in contemporary electronic music. <a href=\"https://www.last.fm/music/Aphex+Twin\">Read more on Last.fm</a>",
            "content": "Richard David James (born 18 August 1971), known professionally as Aphex Twin, is a British musician, composer, and DJ who has been active in electronic music since 1988. His work incorporates a variety of styles, including techno, ambient, acid, and jungle. He is often associated with the intelligent dance music (IDM) genre. Several publications such as Mixmag, The New York Times, NME, Fact, Clash, and The Guardian have recognized him as an influential figure in contemporary electronic music.\n\nJames was raised in Cornwall and began DJing at free parties and clubs in the South West of England in the late 1980s. His debut EP, \"Analogue Bubblebath,\" was released in 1991 on Mighty Force Records and helped him gain an early following. He then performed across the UK and Europe. In the same year, he co-founded the independent label Rephlex Records. His debut album, \"Selected Ambient Works 85\u201392,\" released in 1992 by the Belgian label Apollo, received critical and popular attention. James signed with Warp Records later that year and released albums including \"...I Care Because You Do\" (1995) and \"Richard D. James Album\" (1996). He also released singles such as \"Come to Daddy\" (1997) and \"Windowlicker\" (1999), both accompanied by music videos directed by Chris Cunningham, which expanded his international presence.\n\nFollowing the release of \"Drukqs\" in 2001 and the completion of his Warp contract, James released music through Rephlex Records, including the 2005 \"Analord\" EP series under the alias AFX and two releases in 2007 under the name the Tuss. In 2014, he released a previously unreleased 1994 album as Caustic Window. Later that year, he returned as Aphex Twin with the album \"Syro\" on Warp Records, which won the Grammy Award for Best Dance/Electronic Album. Subsequent releases include the EPs \"Cheetah\" (2016) and \"Collapse\" (2018). His 2023 single \"Blackbox Life Recorder 21f\" was nominated for the Grammy Award for Best Dance/Electronic Recording.\n\nStudio albums\nSelected Ambient Works 85-92\nSelected Ambient Works Volume II (1994)\n...I Care Because You Do (1995)\nRichard D. James Album (1996)\nDrukqs (2001)\nSyro (2014) <a href=\"https://www.last.fm/music/Aphex+Twin\">Read more on Last.fm</a>. User-contributed text is available under the Creative Commons By-SA License; additional terms may apply."
        }
    }
}
'''
'''
Sample response (without username):
{
    "artist": {
        "name": "Aphex Twin",
        "mbid": "f22942a1-6f70-4f48-866e-238cb2308fbd",
        "url": "https://www.last.fm/music/Aphex+Twin",
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
        ],
        "streamable": "0",
        "ontour": "0",
        "stats": {
            "listeners": "2930282",
            "playcount": "212148914"
        },
        "similar": {
            "artist": [
                {
                    "name": "AFX",
                    "url": "https://www.last.fm/music/AFX",
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
                    "name": "Polygon Window",
                    "url": "https://www.last.fm/music/Polygon+Window",
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
                    "name": "Squarepusher",
                    "url": "https://www.last.fm/music/Squarepusher",
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
                    "name": "Boards of Canada",
                    "url": "https://www.last.fm/music/Boards+of+Canada",
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
                    "name": "Autechre",
                    "url": "https://www.last.fm/music/Autechre",
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
            ]
        },
        "tags": {
            "tag": [
                {
                    "name": "electronic",
                    "url": "https://www.last.fm/tag/electronic"
                },
                {
                    "name": "idm",
                    "url": "https://www.last.fm/tag/idm"
                },
                {
                    "name": "ambient",
                    "url": "https://www.last.fm/tag/ambient"
                },
                {
                    "name": "experimental",
                    "url": "https://www.last.fm/tag/experimental"
                },
                {
                    "name": "electronica",
                    "url": "https://www.last.fm/tag/electronica"
                }
            ]
        },
        "bio": {
            "links": {
                "link": {
                    "#text": "",
                    "rel": "original",
                    "href": "https://last.fm/music/Aphex+Twin/+wiki"
                }
            },
            "published": "02 Feb 2006, 16:17",
            "summary": "Richard David James (born 18 August 1971), known professionally as Aphex Twin, is a British musician, composer, and DJ who has been active in electronic music since 1988. His work incorporates a variety of styles, including techno, ambient, acid, and jungle. He is often associated with the intelligent dance music (IDM) genre. Several publications such as Mixmag, The New York Times, NME, Fact, Clash, and The Guardian have recognized him as an influential figure in contemporary electronic music. <a href=\"https://www.last.fm/music/Aphex+Twin\">Read more on Last.fm</a>",
            "content": "Richard David James (born 18 August 1971), known professionally as Aphex Twin, is a British musician, composer, and DJ who has been active in electronic music since 1988. His work incorporates a variety of styles, including techno, ambient, acid, and jungle. He is often associated with the intelligent dance music (IDM) genre. Several publications such as Mixmag, The New York Times, NME, Fact, Clash, and The Guardian have recognized him as an influential figure in contemporary electronic music.\n\nJames was raised in Cornwall and began DJing at free parties and clubs in the South West of England in the late 1980s. His debut EP, \"Analogue Bubblebath,\" was released in 1991 on Mighty Force Records and helped him gain an early following. He then performed across the UK and Europe. In the same year, he co-founded the independent label Rephlex Records. His debut album, \"Selected Ambient Works 85\u201392,\" released in 1992 by the Belgian label Apollo, received critical and popular attention. James signed with Warp Records later that year and released albums including \"...I Care Because You Do\" (1995) and \"Richard D. James Album\" (1996). He also released singles such as \"Come to Daddy\" (1997) and \"Windowlicker\" (1999), both accompanied by music videos directed by Chris Cunningham, which expanded his international presence.\n\nFollowing the release of \"Drukqs\" in 2001 and the completion of his Warp contract, James released music through Rephlex Records, including the 2005 \"Analord\" EP series under the alias AFX and two releases in 2007 under the name the Tuss. In 2014, he released a previously unreleased 1994 album as Caustic Window. Later that year, he returned as Aphex Twin with the album \"Syro\" on Warp Records, which won the Grammy Award for Best Dance/Electronic Album. Subsequent releases include the EPs \"Cheetah\" (2016) and \"Collapse\" (2018). His 2023 single \"Blackbox Life Recorder 21f\" was nominated for the Grammy Award for Best Dance/Electronic Recording.\n\nStudio albums\nSelected Ambient Works 85-92\nSelected Ambient Works Volume II (1994)\n...I Care Because You Do (1995)\nRichard D. James Album (1996)\nDrukqs (2001)\nSyro (2014) <a href=\"https://www.last.fm/music/Aphex+Twin\">Read more on Last.fm</a>. User-contributed text is available under the Creative Commons By-SA License; additional terms may apply."
        }
    }
}
'''
def get_info(artist, username=None):
    params = {"artist": artist}
    if username:
        params["username"] = username

    return lastfm_request("artist.getInfo", params)


'''
Sample response:
{
    "similarartists": {
        "artist": [
            {
                "name": "AFX",
                "mbid": "87225a21-c925-41cd-852f-be4b052d0824",
                "match": "1",
                "url": "https://www.last.fm/music/AFX",
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
                ],
                "streamable": "0"
            },
            {
                "name": "Polygon Window",
                "mbid": "aaa78ce4-e4fe-43b6-abe1-733dc83f8eb1",
                "match": "0.796383",
                "url": "https://www.last.fm/music/Polygon+Window",
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
                ],
                "streamable": "0"
            }
        ],
        "@attr": {
            "artist": "Aphex Twin"
        }
    }
}
'''
def get_similar(artist, limit=None):
    params = {"artist": artist}
    if limit:
        params["limit"] = limit

    return lastfm_request("artist.getSimilar", params)


'''
Sample response:
{
    "topalbums": {
        "album": [
            {
                "name": "Drukqs",
                "playcount": 35343198,
                "mbid": "4d35da90-c4f9-4d37-b68a-027225fca9cd",
                "url": "https://www.last.fm/music/Aphex+Twin/Drukqs",
                "artist": {
                    "name": "Aphex Twin",
                    "mbid": "f22942a1-6f70-4f48-866e-238cb2308fbd",
                    "url": "https://www.last.fm/music/Aphex+Twin"
                },
                "image": [
                    {
                        "#text": "https://lastfm.freetls.fastly.net/i/u/34s/0c5853ff38e027843b907a821257534e.png",
                        "size": "small"
                    },
                    {
                        "#text": "https://lastfm.freetls.fastly.net/i/u/64s/0c5853ff38e027843b907a821257534e.png",
                        "size": "medium"
                    },
                    {
                        "#text": "https://lastfm.freetls.fastly.net/i/u/174s/0c5853ff38e027843b907a821257534e.png",
                        "size": "large"
                    },
                    {
                        "#text": "https://lastfm.freetls.fastly.net/i/u/300x300/0c5853ff38e027843b907a821257534e.png",
                        "size": "extralarge"
                    }
                ],
                "@attr": {
                    "rank": "1"
                }
            },
            {
                "name": "Selected Ambient Works 85-92",
                "playcount": 43463849,
                "mbid": "0c8b4425-795e-4772-8cbf-e3f9694110cc",
                "url": "https://www.last.fm/music/Aphex+Twin/Selected+Ambient+Works+85-92",
                "artist": {
                    "name": "Aphex Twin",
                    "mbid": "f22942a1-6f70-4f48-866e-238cb2308fbd",
                    "url": "https://www.last.fm/music/Aphex+Twin"
                },
                "image": [
                    {
                        "#text": "https://lastfm.freetls.fastly.net/i/u/34s/36307d33d9e5025c8f4564748e17a5f8.png",
                        "size": "small"
                    },
                    {
                        "#text": "https://lastfm.freetls.fastly.net/i/u/64s/36307d33d9e5025c8f4564748e17a5f8.png",
                        "size": "medium"
                    },
                    {
                        "#text": "https://lastfm.freetls.fastly.net/i/u/174s/36307d33d9e5025c8f4564748e17a5f8.png",
                        "size": "large"
                    },
                    {
                        "#text": "https://lastfm.freetls.fastly.net/i/u/300x300/36307d33d9e5025c8f4564748e17a5f8.png",
                        "size": "extralarge"
                    }
                ],
                "@attr": {
                    "rank": "2"
                }
            }
        ],
        "@attr": {
            "artist": "Aphex Twin",
            "page": "1",
            "perPage": "2",
            "totalPages": "25571",
            "total": "51141"
        }
    }
}
'''
def get_top_albums(artist, limit=None):
    params = {"artist": artist}
    if limit:
        params["limit"] = limit

    return lastfm_request("artist.getTopAlbums", params)


'''
Sample response:
{
    "toptags": {
        "tag": [
            {
                "count": 100,
                "name": "electronic",
                "url": "https://www.last.fm/tag/electronic"
            },
            {
                "count": 97,
                "name": "idm",
                "url": "https://www.last.fm/tag/idm"
            },
            {
                "count": 62,
                "name": "ambient",
                "url": "https://www.last.fm/tag/ambient"
            },
            {
                "count": 47,
                "name": "experimental",
                "url": "https://www.last.fm/tag/experimental"
            },
            {
                "count": 11,
                "name": "electronica",
                "url": "https://www.last.fm/tag/electronica"
            },
            {
                "count": 4,
                "name": "techno",
                "url": "https://www.last.fm/tag/techno"
            },
            {
                "count": 3,
                "name": "Ambient Techno",
                "url": "https://www.last.fm/tag/Ambient+Techno"
            },
            {
                "count": 1,
                "name": "british",
                "url": "https://www.last.fm/tag/british"
            },
            {
                "count": 1,
                "name": "acid techno",
                "url": "https://www.last.fm/tag/acid+techno"
            },
            {
                "count": 1,
                "name": "Acid",
                "url": "https://www.last.fm/tag/Acid"
            }
        ],
        "@attr": {
            "artist": "Aphex Twin"
        }
    }
}
'''
def get_top_tags(artist):
    return lastfm_request("artist.getTopTags", {"artist": artist})


'''
Sample response:
{
    "toptracks": {
        "track": [
            {
                "name": "Avril 14th",
                "playcount": "11030190",
                "listeners": "1076629",
                "url": "https://www.last.fm/music/Aphex+Twin/_/Avril+14th",
                "streamable": "0",
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
                "name": "Xtal",
                "playcount": "10678990",
                "listeners": "942652",
                "mbid": "e5e5e3c9-8515-4abf-aebb-7529b4e9aa0b",
                "url": "https://www.last.fm/music/Aphex+Twin/_/Xtal",
                "streamable": "0",
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
            "artist": "Aphex Twin",
            "page": "1",
            "perPage": "2",
            "totalPages": "75337",
            "total": "150674"
        }
    }
}
'''
def get_top_tracks(artist, limit=None):
    params = {"artist": artist}
    if limit:
        params["limit"] = limit

    return lastfm_request("artist.getTopTracks", params)
