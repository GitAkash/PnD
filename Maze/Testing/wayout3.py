from line_profiler_pycharm import profile
import numpy as np
import time
from maze_env import *

@profile
def way_out(env):
    #Initalise Variables
    loc, done = env.reset()
    pathList = []
    junctionList = []
    cached_map = {}
    move = 0

    # Initialize starting position.
    firstJuncTets = len(env.action_space()) == 3
    start = list(loc)
    start.append(firstJuncTets)


    '''
    Searching the path through the map
        - Follow the right wall
        - Cache current location for faster lookup
        - Check for junctions
    '''

    while not done:
        # Caching the path for faster calls
        if loc in cached_map:
            availableActions = cached_map[loc]['actions']
        else:
            availableActions = np.array(env.action_space())
            cached_map[loc] = {'location': loc, 'actions': availableActions}

        # Checking if the path is a junction
        isJunction = len(availableActions) == 3 # Check If the Location is a junction
        junctionList.append(isJunction)

        #Moving around the maze
        actions = (availableActions - move) & 3  # shift movement for direction
        if 1 in actions:
            move = (1 + move) & 3
        else:
            if 0 in actions:
                move = (0 + move) & 3
            else:
                move = (3 + move) & 3

        loc, done = env.step(move)
        pathList.append(loc)

    # Putting the final path into a numpy array.
    path = np.vstack((start,np.column_stack((pathList, junctionList))))

    '''
    Getting the direct path
        - If a junction is encountered twice, remove its path
    '''
    # check for unique rows and index them
    unique_rows, unique_indices, counts = np.unique(path, axis=0, return_index=True, return_counts=True)
    for i, count in enumerate(counts):
        if count >= 2 and unique_rows[i][-1]:
            is_duplicate = np.all(path == unique_rows[i], axis=1)
            duplicate_indices = np.where(is_duplicate)[0]

            if duplicate_indices.size >= 2:
                start_index, end_index = duplicate_indices[0], duplicate_indices[-1]
                mask = np.ones_like(is_duplicate, dtype=bool)
                mask[start_index:end_index] = False
                path = path[mask]

    unique_rows, unique_indices, counts = np.unique(path, axis=0, return_index=True, return_counts=True)
    for i, count in enumerate(counts):
        if count >= 2:
            is_duplicate = np.all(path == unique_rows[i], axis=1)
            duplicate_indices = np.where(is_duplicate)[0]

            if duplicate_indices.size >= 2:
                start_index, end_index = duplicate_indices[0], duplicate_indices[-1]
                mask = np.ones_like(is_duplicate, dtype=bool)
                mask[start_index:end_index] = False
                path = path[mask]

    path = path[:,0:2]
    return path


def main():
    env = make(size=21, seed=5)
    start = time.time()
    finalPath = way_out(env)
    end = time.time()
    print(end - start)
    env.render(finalPath)


if __name__ == '__main__':
    main()
