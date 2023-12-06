from maze_env import *
import numpy as np
import time

'''
front = 0
right = 1
down = 2
left = 3
'''

env = make(size=101)

def rightFollow(env):
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

        path = np.vstack((path, loc))
    return path


def leftFollow(env):
    loc, done = env.reset()
    path = np.array([loc])

    move = 0
    while not done:
        availableActions = np.array(env.action_space())
        actions = (availableActions - move) % 4  # Shift actions to relative directions.
        if 3 in actions:
            move = (3 + move) % 4  # Shift move back to absolute directions.
        else:
            if 0 in actions:
                move = (0 + move) % 4
            else:
                move = (1 + move) % 4
        loc, done = env.step(move)

        path = np.vstack((path, loc))
        # env.render(path=path)
        # matplotlib.pyplot.show(block=False)
        # print(actions)
    return path

def Remove():
    np.unique(rightFollow(env))
    



def main():
    # Cleanup(Algorithm(env))
    env.render(path=rightFollow(env))
    matplotlib.pyplot.show(block=True)

if __name__ == '__main__':
    main()
