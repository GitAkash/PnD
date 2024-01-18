import multiprocessing

from maze_env import *
import time
import matplotlib
import concurrent.futures

matplotlib.use("QtAgg")


def way_out(env, direction):
    # The direction parameter can be "right" or "left"
    loc, done = env.reset()
    path_list = []
    junction_list = []
    cached_map = {}
    move = 0

    while not done:
        if loc in cached_map:
            actions_bitmask = cached_map[loc]["actions"]
        else:
            available_actions = env.action_space()
            bitmask = 0
            for action in available_actions:
                bitmask |= 1 << action
            actions_bitmask = bitmask
            cached_map[loc] = {"location": loc, "actions": actions_bitmask}

        is_junction = (
            actions_bitmask == 0b0111
            or actions_bitmask == 0b1011
            or actions_bitmask == 0b1101
            or actions_bitmask == 0b1110
            or actions_bitmask == 0b1111
        )
        junction_list.append(is_junction)

        actions = ((actions_bitmask >> move) & 0b1111) | (actions_bitmask << (4 - move))

        if direction == "right":
            if (actions & (1 << 1)) != 0:
                move = (1 + move) & 3
            else:
                if (actions & (1 << 0)) != 0:
                    move = (0 + move) & 3
                else:
                    move = (3 + move) & 3
        elif direction == "left":
            if (actions & (1 << 0)) != 0:
                move = (0 + move) & 3
            else:
                if (actions & (1 << 1)) != 0:
                    move = (1 + move) & 3
                else:
                    move = (2 + move) & 3

        loc, done = env.step(move)
        path_list.append(loc)

    path = np.vstack((path_list, junction_list))
    return path


def main():
    env = make(size=101, seed = 2)
    start = time.time()
    finalPath = way_out(env, "left")
    end = time.time()
    print(end - start)

if __name__ == "__main__":
    main()
