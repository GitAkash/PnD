import csv
from maze_env import *
import numpy as np
import time


def ask():
    start = int(input("Start Size: "))
    end = int(input("End Size: "))
    step = int(input("Step: "))
    num_trials = int(input("Number of Trials: "))

    if start % 2 == 0:
        start += 1
        print("Your starting size must be even..")

    if step % 2 != 0:
        step += 1
        print("Your step size must be even..")

    if start <= 5:
        print("Your start size must be larger than 5..")
        return None

    if end < start:
        print("The end size must be bigger than the start size..")
        return None

    if step > end - start:
        print("Your step cant be bigger than your searching size..")
        return None

    return start, end, step, num_trials


def way_out(env):
    loc, done = env.reset()
    path = np.array([loc])
    move = 0
    while not done:
        availableActions = np.array(env.action_space())
        actions = (availableActions - move) % 4
        if 1 in actions:
            move = (1 + move) % 4
        else:
            if 0 in actions:
                move = (0 + move) % 4
            else:
                move = (3 + move) % 4
        loc, done = env.step(move)
        path = np.vstack((loc, path))

    unique_rows, unique_indices, counts = np.unique(path, axis=0, return_index=True, return_counts=True)
    for i, count in enumerate(counts):
        if count >= 2:
            duplicate_indices = np.where(np.all(path == unique_rows[i], axis=1))[0]

            if duplicate_indices.size >= 2:
                start_index = duplicate_indices[0]
                end_index = duplicate_indices[-1]
                path = np.vstack((path[:start_index + 1, :], path[end_index:, :]))
    return path


def main():
    env = make(size=101)
    finalPath = way_out(env)
    env.render(finalPath)
    matplotlib.pyplot.show()
    print(finalPath)


if __name__ == '__main__':
    main()
