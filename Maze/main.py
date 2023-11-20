from maze_env import make
import matplotlib; matplotlib.use("TkAgg")

env = make(size=9, seed=12345, perfect=True)
env.render()
