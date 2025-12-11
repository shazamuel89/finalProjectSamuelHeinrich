from ..adapters.lastfm import user


'''
Sample output (for artist target):
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
def get_lastfm_data(username, target, time_range, limit):
    numberOfWeeks = time_range_to_weeks(time_range)

    # Fetch weekly chart list for timestamps of weeks
    weeklyChartListData = user.get_weekly_chart_list(username)
    weeklyChartList = weeklyChartListData['weeklychartlist']['chart']

    if numberOfWeeks is None:   # 'alltime' time_range
        filteredWeeklyChartList = weeklyChartList
    else:
        # Extract last N weeks (sorted oldest to newest)
        filteredWeeklyChartList = weeklyChartList[-numberOfWeeks:]

    # Data structure to return
    streamData = {}

    # Week counter will increase at the beginning of each week's loop
    weekIndex = -1

    for week in filteredWeeklyChartList:
        # Increment at the beginning to ensure it increments even if continues happen
        weekIndex += 1
        # Get the week start and end timestamps
        weekStart = week['from']
        weekEnd = week['to']

        # Get the entity for the specific week
        try:
            if target == 'artist':
                weekEntitiesData = user.get_weekly_artist_chart(
                    username,
                    from_ts=weekStart,
                    to_ts=weekEnd,
                )
                entityChartKey = 'weeklyartistchart'
                entityListKey = 'artist'
            elif target == 'album':
                weekEntitiesData = user.get_weekly_album_chart(
                    username,
                    from_ts=weekStart,
                    to_ts=weekEnd,
                )
                entityChartKey = 'weeklyalbumchart'
                entityListKey = 'album'
            elif target == 'track':
                weekEntitiesData = user.get_weekly_track_chart(
                    username,
                    from_ts=weekStart,
                    to_ts=weekEnd,
                )
                entityChartKey = 'weeklytrackchart'
                entityListKey = 'track'
            else:
                print(f"Unsupported target {target}, skipping.")
                continue
        except Exception:
            # Last.fm's API can occasionally return status code 500 or an empty response
            print(f"Last.fm failed for week {weekStart} to {weekEnd}, skipping.")
            continue

        # Verify the data exists
        if not weekEntitiesData or entityChartKey not in weekEntitiesData or entityListKey not in weekEntitiesData[entityChartKey]:
            continue

        weekEntities = weekEntitiesData[entityChartKey][entityListKey]

        # Normalize to list (in case Last.fm returns weirdly)
        if isinstance(weekEntities, dict):
            weekEntities = [weekEntities]
        elif weekEntities is None:
            weekEntities = []

        # Extract the entity's data
        for entity in weekEntities:
            entityName = entity['name']
            playcount = int(entity['playcount'])

            # Add entity if they have not been added to stream data yet
            if entityName not in streamData:
                streamData[entityName] = []

            # Append entity's week's data to the entity's array
            streamData[entityName].append({
                'weekIndex': weekIndex,
                'weekStart': weekStart,
                'weekEnd': weekEnd,
                'playcount': playcount
            })

    return {
        'streamData': streamData,
        'weeks': filteredWeeklyChartList
    }


'''
Convert a user-selected time_range string into number of weeks.
Approximations:
- 1 month ≈ 4 weeks
- 3 months ≈ 13 weeks
- 6 months ≈ 26 weeks
- 12 months ≈ 52 weeks
- alltime = None (meaning "use all available weeks")
'''
def time_range_to_weeks(time_range):
    mapping = {
        "7day": 1,
        "1month": 4,
        "3month": 13,
        "6month": 26,
        "12month": 52,
        "alltime": None,  # caller interprets None as "don't slice"
    }
    return mapping.get(time_range, None)
