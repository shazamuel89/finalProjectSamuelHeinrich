import matplotlib.pyplot as plt
import numpy as np


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