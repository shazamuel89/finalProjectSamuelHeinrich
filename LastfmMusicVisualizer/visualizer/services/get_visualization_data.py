from ..adapters.lastfm import user


def get_lastfm_demo_data():
    username = 'shazamuel89'
    numberOfWeeks = 24 # Last 6 months

    # Fetch weekly chart list for timestamps of weeks
    weeklyChartListData = user.get_weekly_chart_list(username)
    weeklyChartList = weeklyChartListData['weeklychartlist']['chart']

    # Extract last N weeks (sorted oldest to newest)
    filteredWeeklyChartList = weeklyChartList[-numberOfWeeks:]

    # Dictionary to return
    streamData = {}

    # Week counter will increase for each week
    weekCount = 1

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

            '''
            Append artist's data to stream data like this:
            streamData = {
                'Aphex Twin': [
                    { 'week': 1, 'playcount': 27 },
                    { 'week': 2, 'playcount': 12 },
                    ...more weeks...
                ],
                ...more artists...
            }
            '''
            streamData[artistname].append({ 'week': weekCount, 'playcount': playcount })

        # Increment week count to next oldest week
        weekCount += 1

    return streamData