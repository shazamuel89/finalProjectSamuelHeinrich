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

def create_data_fed_streamgraph(data):
    # Prepare the data for direct insertion into a stackplot
    preparedData = prepare_stackplot_data(data)

    # Create the figure
    fig = go.Figure()
    #fig, ax = plt.subplots(figsize=(12, 6))

    # Loop through each artist and add a stacked area trace
    for artist, y in zip(preparedData['artists'], preparedData['y']):
        fig.add_trace(go.Scatter(
            x=preparedData['x'],
            y=y,
            stackgroup='one',
            name=artist,
            hoverinfo="x+y+name",
            line=dict(width=0),     # Removes outline
            mode="none",
        ))

    # Layout styling
    fig.update_layout(
        title="Data Fed Streamgraph Demo",
        xaxis_title="End of Week",
        yaxis_title="Scrobbles",
        hovermode="x unified",
        template="plotly_white",
        height=600,
        width=1200,
    )

    return fig
