from maze_env import *
import matplotlib;

import random
import numpy as np

env = make(size=9, seed=123545, perfect=True)

def Random(env):
    loc, done = env.reset()
    path = np.array([loc])

    while not done:
        actions = env.action_space()
        move = random.choice(actions)
        loc, done = env.step(move)
        path = np.vstack((path, loc))
        print(loc)
    return path


def Algorithm(env):
    loc, done = env.reset()
    path = np.array([loc])
    lastMove = 0
    while not done:
        actions = env.action_space()

        if lastMove == 2:  # Down
            front = 2; right = 3; back = 0; left = 1
            if right in actions:
                lastMove = move = right

            else:
                if front not in actions:
                    lastMove = move = random.choice(actions)
                else:
                    lastMove = move = front


        elif lastMove == 3:  # Left
            front = 3; right = 0; back = 1; left = 2
            if right in actions:
                lastMove = move = right

            else:
                if front not in actions:
                    lastMove = move = random.choice(actions)
                else:
                    lastMove = move = front


        elif lastMove == 1:  # Right
            front = 1; right = 2; back = 3; left = 0
            if right in actions:
                lastMove = move = right

            else:
                if front not in actions:
                    lastMove = move = random.choice(actions)
                else:
                    lastMove = move = front

        elif lastMove == 0:  # Up
            front = 0; right = 1; back = 2; left = 3
            if right in actions:
                lastMove = move = right

            else:
                if front not in actions:
                    lastMove = move = random.choice(actions)
                else:
                    lastMove = move = front

        loc, done = env.step(move)
        path = np.vstack((path, loc))
        print(loc)
        env.render(path=path)
        matplotlib.pyplot.show(block=False)
    return path


env.render(path=Algorithm(env))
matplotlib.pyplot.show(block=True)
