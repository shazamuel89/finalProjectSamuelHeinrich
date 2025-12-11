import numpy as np


# y is a list of arrays
def compute_baseline(y):
    # Convert to 2D numpy array
    Y = np.array(y)

    # Get the total height of the stack at each x position
    totals = Y.sum(axis=0)

    # Shift everything down by half the total height so the stack is centered around y = 0
    baseline = -totals / 2

    # Will contain arrays representing each entity's shifted top boundary
    adjusted = []

    # current is an array representing the total bottom boundary for each x position
    current = baseline.copy()

    # For each entity's data
    for layer in Y:
        # Mark the top points of the next entity to stack on
        adjusted.append(current + layer)
        # Move the bottom boundary to the top of the layer just made
        current += layer
