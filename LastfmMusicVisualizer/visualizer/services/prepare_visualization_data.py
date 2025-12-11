from datetime import datetime, UTC


def to_date(timestamp):
    return datetime.fromtimestamp(int(timestamp), UTC)


def prepare_stackplot_data(data):
    # Extract stream data and weeks timestamps
    streamData = data['streamData']
    weeks = data['weeks']
    numberOfWeeks = len(weeks)

    paddedData = {}

    # For each { entity: entityWeeks }
    for entity, entityWeeks in streamData.items():
        # Create a lookup for the entity's weeks data
        lookup = { week['weekIndex']: week['playcount'] for week in entityWeeks }

        # Will contain the complete week list for the entity
        paddedWeeks = []

        # For each week, including missing weeks
        for i in range(0, numberOfWeeks):
            # If the week entry exists in the entity's data, then set the playcount
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

        # Attach the padded weeks to the entity
        paddedData[entity] = paddedWeeks

    # x-axis labels are the end dates of each week
    xAxisLabels = [to_date(week['to']) for week in weeks]
    entities = list(paddedData.keys())
    # Arrays of data points for each entity
    yArrays = [
        # For each entity, create an array where each week's playcount is the value
        [week['playcount'] for week in paddedData[entity]]
        for entity in entities
    ]

    return {
        'x': xAxisLabels,
        'y': yArrays,
        'entities': entities
    }