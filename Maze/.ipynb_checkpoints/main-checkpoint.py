from maze_env import *
import matplotlib; matplotlib.use("WebAgg")

env = make(size=9, seed=12345, perfect=True)
loc, done = env.reset()
env.render()
