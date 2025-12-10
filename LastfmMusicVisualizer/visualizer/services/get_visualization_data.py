from ..adapters.lastfm import user


'''
Sample output:
{
    streamData: {
        'Aphex Twin': [
        {
            'weekIndex': 0,
            'weekStart': '1108296000',
            'weekEnd': '1108900800',
            'playcount': 27,
        },
        {
            'weekIndex': 1,
            'weekStart': '1108900800',
            'weekEnd': '1109505600',
            'playcount': 12,
        },
        ...more weeks...
    ],
    ...more artists...
    },
    weeks: [
        {
            "#text": "",
            "from": "1108296000",
            "to": "1108900800"
        },
        {
            "#text": "",
            "from": "1108900800",
            "to": "1109505600"
        },
    ],
    ...more weeks...
}
'''
def get_lastfm_demo_data():
    username = 'shazamuel89'
    numberOfWeeks = 24

    # Fetch weekly chart list for timestamps of weeks
    weeklyChartListData = user.get_weekly_chart_list(username)
    weeklyChartList = weeklyChartListData['weeklychartlist']['chart']

    # Extract last N weeks (sorted oldest to newest)
    filteredWeeklyChartList = weeklyChartList[-numberOfWeeks:]

    # Dictionary to return
    streamData = {}

    # Week counter will increase for each week
    weekCount = 0

    for week in filteredWeeklyChartList:
        # Get the week start and end timestamps
        weekStart = week['from']
        weekEnd = week['to']

        # Get the artists for the specific week
        weekArtistsData = user.get_weekly_artist_chart(username, from_ts=weekStart, to_ts=weekEnd)
        weekArtists = weekArtistsData['weeklyartistchart']['artist']

        # Extract the artist's data
        for artist in weekArtists:
            artistname = artist['name']
            playcount = int(artist['playcount'])

            # Add artist if they have not been added to stream data yet
            if artistname not in streamData:
                streamData[artistname] = []

            # Append artist's week's data to the artist's array
            streamData[artistname].append({
                'weekIndex': weekCount,
                'weekStart': weekStart,
                'weekEnd': weekEnd,
                'playcount': playcount
            })

        # Increment week count to next oldest week
        weekCount += 1

    return {
        'streamData': streamData,
        'weeks': filteredWeeklyChartList
    }
