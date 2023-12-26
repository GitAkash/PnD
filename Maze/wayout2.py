from maze_env import *
import time
from line_profiler_pycharm import profile

@profile
def way_out(env):
    loc, done = env.reset()
    pathList = []
    junctionList = []
    move = 0
    while not done:
        availableActions = np.array(env.action_space())
        if len(availableActions) == 3:
            junctionList.append(True)

        if len(availableActions) != 3:
            junctionList.append(False)

        actions = (availableActions - move) % 4
        if 1 in actions:
            move = (1 + move) % 4
        else:
            if 0 in actions:
                move = (0 + move) % 4
            else:
                move = (3 + move) % 4
        loc, done = env.step(move)
        pathList.append(loc)

    path = np.vstack(pathList)
    junction = np.vstack(junctionList)
    path = np.hstack((path, junction))
    unique_rows, unique_indices, counts = np.unique(path, axis=0, return_index=True, return_counts=True)
    for i, count in enumerate(counts):
        if count >= 2 and unique_rows[i][-1]:
            duplicate_indices = np.where(np.all(path == unique_rows[i], axis=1))[0]
            if duplicate_indices.size >= 2 and unique_rows[i][-1]:
                start_index = duplicate_indices[0]
                end_index = duplicate_indices[-1]
                path = np.vstack((path[:start_index + 1, :], path[end_index:, :]))
    return path


def main():
    env = make(size=101, seed=3)
    start = time.time()
    finalPath = way_out(env)
    end = time.time()
    print(end-start)
    env.render(finalPath)
    matplotlib.pyplot.show()


if __name__ == '__main__':
    main()

