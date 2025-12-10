from datetime import datetime, UTC


def to_date(timestamp):
    return datetime.fromtimestamp(int(timestamp), UTC)


def prepare_stackplot_data(data):
    # Extract stream data and weeks timestamps
    streamData = data['streamData']
    weeks = data['weeks']
    numberOfWeeks = len(weeks)

    paddedData = {}

    # For each { artist: artistWeeks }
    for artist, artistWeeks in streamData.items():
        # Create a lookup for the artist's weeks data
        lookup = { week['weekIndex']: week['playcount'] for week in artistWeeks }

        # Will contain the complete week list for the artist
        paddedWeeks = []

        # For each week, including missing weeks
        for i in range(0, numberOfWeeks):
            # If the week entry exists in the artist's data, then set the playcount
            if (i in lookup):
                playcount = lookup[i]
            # If the week entry does not exist, then set the playcount to 0
            else:
                playcount = 0

            # Append the week data to the paddedWeeks array
            paddedWeeks.append({
                'weekIndex': i,
                'weekStart': to_date(weeks[i]['from']),
                'weekEnd': to_date(weeks[i]['to']),
                'playcount': playcount,
            })

        # Attach the padded weeks to the artist
        paddedData[artist] = paddedWeeks

    # x-axis labels are the end dates of each week
    xAxisLabels = [to_date(week['to']) for week in weeks]
    artists = list(paddedData.keys())
    # Arrays of data points for each artist
    yArrays = [
        # For each artist, create an array where each week's playcount is the value
        [week['playcount'] for week in paddedData[artist]]
        for artist in artists
    ]

    return {
        'x': xAxisLabels,
        'y': yArrays,
        'artists': artists
    }