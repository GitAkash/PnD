from maze_env import *
import numpy as np
import time

def leftFollow(env):
    """Solve the algorithm"""
    pathfinding = time.time()
    loc, done = env.reset()
    path = np.array([loc])
    move = 0
    while not done:
        availableActions = np.array(env.action_space())
        actions = (availableActions - move) % 4  # Shift actions to relative directions.
        if 3 in actions:  # Change from 1 to 3 for left movement
            move = (3 + move) % 4  # Shift move back to absolute directions.
        else:
            if 0 in actions:
                move = (0 + move) % 4
            else:
                move = (1 + move) % 4  # Change from 3 to 1 for right movement
        loc, done = env.step(move)

        path = np.vstack((loc, path))

    donepathfinding = time.time()
    print(donepathfinding - pathfinding)

    removepath = time.time()
    """Clean up"""
    unique_rows, unique_indices, counts = np.unique(path, axis=0, return_index=True, return_counts=True)

    for i, count in enumerate(counts):
        if count >= 2:
            duplicate_indices = np.where(np.all(path == unique_rows[i], axis=1))[0]

            if duplicate_indices.size >= 2:
                start_index = duplicate_indices[0]
                end_index = duplicate_indices[-1]
                path = np.vstack((path[:start_index + 1, :], path[end_index:, :]))
    doneremovepath = time.time()
    print(doneremovepath - removepath)
    return path

def main():
    # sizeTime()
    env = make(size=11, seed=18)
    start = time.time()
    env.render(leftFollow(env))
    end = time.time()
    print(end-start)
    matplotlib.pyplot.show()

if __name__ == '__main__':
    main()
