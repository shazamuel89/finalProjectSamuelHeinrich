import matplotlib.pyplot as plt
import numpy as np
from .prepare_visualization_data import prepare_stackplot_data


def create_dummy_streamgraph():
    # ----------------------------------
    # 1. Dummy Weekly Data
    # ----------------------------------
    weeks = np.arange(10)  # 10 weeks

    # Suppose 3 artists:
    artist1 = np.array([5, 10, 6, 8, 12, 7, 9, 5, 3, 4])
    artist2 = np.array([3, 4,  5, 3, 2,  1, 2, 4, 6, 8])
    artist3 = np.array([6, 3,  2, 4, 5,  7, 4, 6, 5, 3])

    # Stack the arrays vertically to create a single 2 dimensional array so stackplot can use them together
    data = np.vstack([artist1, artist2, artist3])

    # ----------------------------------
    # 2. Basic Streamgraph
    # ----------------------------------
    fig, ax = plt.subplots(figsize=(12, 6))

    ax.stackplot(weeks, data, baseline='wiggle')

    ax.set_title("Dummy Streamgraph Example", fontsize=16)
    ax.set_xlabel("Week")
    ax.set_ylabel("Scrobbles (raw)")

    return fig

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

    return fig