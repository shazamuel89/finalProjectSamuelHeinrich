'''
import matplotlib.pyplot as plt
from .prepare_visualization_data import prepare_stackplot_data


def create_data_fed_streamgraph(data):
    # Prepare the data for direct insertion into a stackplot
    preparedData = prepare_stackplot_data(data)

    # Create the figure
    fig, ax = plt.subplots(figsize=(12, 6))

    # Plot the prepared data into a stackplot
    ax.stackplot(
        preparedData['x'],
        *preparedData['y'],
        baseline='wiggle',
        labels=preparedData['artists']
    )
    #ax.legend(loc='upper left')

    # Set labels and title
    ax.set_title("Data Fed Streamgraph Demo", fontsize=16)
    ax.set_xlabel("End of Week")
    ax.set_ylabel("Scrobbles")

    ax.tick_params(axis='x', rotation=45)

    plt.tight_layout()

    print(type(fig))

    return fig
'''

import plotly.graph_objects as go
from .prepare_visualization_data import prepare_stackplot_data
from .compute_baseline import compute_baseline

def create_data_fed_streamgraph(data):
    # Prepare the data for direct insertion into a stackplot
    preparedData = prepare_stackplot_data(data)

    #preparedData = compute_baseline(preparedData['y'])

    # Create the figure
    fig = go.Figure()

    # Loop through each artist and add a stacked area trace
    for entity, y in zip(preparedData['entities'], preparedData['y']):
        fig.add_trace(go.Scatter(
            x=preparedData['x'],
            y=y,
            stackgroup='one',
            name=entity,
            hoverinfo="x+y+name",
            line=dict(width=0),     # Removes outline
            mode="lines",
            hovertemplate="<b>%{fullData.name}</b><br>Scrobbles: %{y}<extra></extra>"
        ))

    # Layout styling
    fig.update_layout(
        title="Last.fm Data Fed Streamgraph",
        xaxis_title="End of Week",
        yaxis_title="Scrobbles",
        template="plotly_white",
        height=600,
        width=1200,
    )

    return fig
