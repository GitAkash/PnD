import time

from maze_env import *
import random
import numpy as np

start_time = time.time()
env = make(size=11)


def Random(env):
    loc, done = env.reset()
    path = np.array([loc])

    while not done:
        actions = env.action_space()
        move = random.choice(actions)
        loc, done = env.step(move)
        path = np.vstack((path, loc))
        print(loc)
        env.render(path=path)
        matplotlib.pyplot.show(block=False)
        print(actions)
    return path

env.render(path=Random(env))
matplotlib.pyplot.show(block=True)
print("time elapsed: {:.2f}s".format(time.time() - start_time))
