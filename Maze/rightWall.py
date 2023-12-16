from maze_env import *
import numpy as np
import timeit
from matplotlib import pyplot as plt
import pandas as pd

env = make(size=181)


def rightFollow(env):
    """Solve the algorith """
    loc, done = env.reset()
    path = np.array([loc])
    move = 0
    while not done:
        availableActions = np.array(env.action_space())
        actions = (availableActions - move) % 4  # Shift actions to relative directions.
        if 1 in actions:
            move = (1 + move) % 4  # Shift move back to absolute directions.
        else:
            if 0 in actions:
                move = (0 + move) % 4
            else:
                move = (3 + move) % 4
        loc, done = env.step(move)

        path = np.vstack((loc, path))

    unique_rows, unique_indices, counts = np.unique(path, axis=0, return_index=True, return_counts=True)

    """Clean up"""
    for i, count in enumerate(counts):
        if count >= 2:
            duplicate_indices = np.where(np.all(path == unique_rows[i], axis=1))[0]

            if duplicate_indices.size >= 2:
                start_index = duplicate_indices[0]
                end_index = duplicate_indices[-1]
                path = np.vstack((path[:start_index + 1, :], path[end_index:, :]))

    return path


def sizeTime():
    sizes = np.array([])
    durations = []

    for i in range(101, 301, 2):
        env_setup = f"from __main__ import make, rightFollow; env = make(size={i})"
        time_taken = timeit.timeit("rightFollow(env)", setup=env_setup, number=100)
        average_time = time_taken/100
        print(f"The time for maze size {i} is: {average_time} seconds")
        sizes = np.append(sizes, i)
        durations.append(average_time)

    # Create a DataFrame
    df = pd.DataFrame({'Size': sizes, 'Duration': durations})

    # Export DataFrame to CSV
    df.to_csv('maze_timing_data.csv', index=False)

    # Create scatter plot
    plt.plot(df['Size'], df['Duration'])
    plt.title('Maze Solving Time vs Maze Size')
    plt.xlabel('Maze Size')
    plt.ylabel('Solving Time (seconds)')
    plt.show()



def main():
    sizeTime()


if __name__ == '__main__':
    main()
