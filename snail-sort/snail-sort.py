import numpy as np


def snail(snail_map):

    n = len(snail_map)

    # Convert to 1D array
    snail_map = np.array(snail_map).flatten()

    if len(snail_map) == 0:
        return []

    # Calculate number of spiral loops
    passes = n//2 + (n % 2 != 0)

    index = []  # Container for keeping sorted indexes

    for i in range(passes):

        # Traverse right
        for j in range(n - i*2):
            if len(index) == 0:
                index.append(0)
            else:
                index.append(index[-1] + 1)

        # Traverse down
        for j in range(n - i*2 - 1):
            index.append(index[-1] + n)

        # Traverse left
        for j in range(n - i*2 - 1):
            index.append(index[-1] - 1)

        # Traverse up
        for j in range(n - i*2 - 2):
            index.append(index[-1] - n)

    # Match the sorted indexes with the items in the given array and return the sorted array
    return [snail_map[items] for items in index]
