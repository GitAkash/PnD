from line_profiler_pycharm import profile
from maze_env import *
import time
import matplotlib

matplotlib.use("QtAgg")


@profile
def way_out(env):
    # Initialize Variables
    loc, done = env.reset()
    path_list = []
    junction_list = []
    cached_map = {}
    move = 0

    # Initialize starting position.
    first_junc_test = len(env.action_space()) == 3
    start = list(loc)
    start.append(first_junc_test)

    """
    Searching the path through the map
        - Follow the right wall
        - Cache current location for faster lookup
        - Check for junctions
        - Using a bitmask in order to read available actions
    """
    while not done:
        # Use cache for faster retrieval of the available actions
        if loc in cached_map:
            actions_bitmask = cached_map[loc]["actions"]

        # Caching the path for faster calls
        else:
            # Call available actions
            available_actions = env.action_space()

            # Creating a bitmask from the available actions because using an if statement costs way more time
            bitmask = 0
            for action in available_actions:
                bitmask |= 1 << action
            actions_bitmask = bitmask

            # Caching the location into the dict for faster use next time
            cached_map[loc] = {"location": loc, "actions": actions_bitmask}

        # TODO: Asking for is not junction faster? IE is not junction if length of actions == 1 or 2
        # Checking if the location is a junction
        is_junction = (
            actions_bitmask == 0b0111
            or actions_bitmask == 0b1011
            or actions_bitmask == 0b1101
            or actions_bitmask == 0b1110
            or actions_bitmask == 0b1111

        )
        junction_list.append(is_junction)

        # Shifting the bits of the bitmask in order to cast a relative view onto my actions
        actions = ((actions_bitmask >> move) & 0b1111) | (actions_bitmask << (4 - move))

        # Using the bytes I can check if the move I want is in the array
        # Shifting the bytes back will return the move that is correct for the environment
        if (actions & (1 << 1)) != 0:
            move = (1 + move) & 3
        else:
            if (actions & (1 << 0)) != 0:
                move = (0 + move) & 3
            else:
                move = (3 + move) & 3


        # TODO: Make it so that i can skip asking for the next step if i already have been there
        #       Using my move i can predict my next location so i can skip the API call
        # if move == 0:
        #     nextLoc = (loc[0] - 1, loc[1])
        #
        # elif move == 1:
        #     nextLoc = (loc[0] , loc[1] + 1)
        # elif move == 2:
        #     nextLoc = (loc[0] + 1, loc[1])
        # else:
        #     nextLoc = (loc[0], loc[1] - 1)
        # print(loc, move, nextLoc, lastMove)

        # TODO: Can't skip the env.step? Because then the environment thinks i am teleporting?!
        # if move < lastMove:
        #     # loc, done = env.step(move)
        #     print("Check!?")
        #
        # elif nextLoc in cached_map:
        #     print("Correct!")
        #     loc = cached_map[nextLoc]['location']
        #
        # else:
        #     loc, done = env.step(move)
        # lastMove = move
        # # print(loc)
        loc, done = env.step(move)
        path_list.append(loc)

    # Putting the final path into a numpy array
    path = np.vstack((start, np.column_stack((path_list, junction_list))))

    """
    Getting the direct path
        - If a junction is encountered twice, remove its path
    """
    # TODO: Just make this shit better..
    # check for unique rows and index them
    unique_rows, unique_indices, counts = np.unique(
        path, axis=0, return_index=True, return_counts=True
    )
    for i, count in enumerate(counts):
        if count >= 2 and unique_rows[i][-1]:
            is_duplicate = np.all(path == unique_rows[i], axis=1)
            duplicate_indices = np.where(is_duplicate)[0]

            if duplicate_indices.size >= 2:
                start_index, end_index = duplicate_indices[0], duplicate_indices[-1]
                mask = np.ones_like(is_duplicate, dtype=bool)
                mask[start_index:end_index] = False
                path = path[mask]

    unique_rows, unique_indices, counts = np.unique(
        path, axis=0, return_index=True, return_counts=True
    )
    for i, count in enumerate(counts):
        if count >= 2:
            is_duplicate = np.all(path == unique_rows[i], axis=1)
            duplicate_indices = np.where(is_duplicate)[0]

            if duplicate_indices.size >= 2:
                start_index, end_index = duplicate_indices[0], duplicate_indices[-1]
                mask = np.ones_like(is_duplicate, dtype=bool)
                mask[start_index:end_index] = False
                path = path[mask]

    path = path[:, 0:2]
    return path


def main():
    env = make(size=101)
    start = time.time()
    finalPath = way_out(env)
    end = time.time()
    print(end - start)
    env.render(finalPath)
    matplotlib.pyplot.show(block=True)


if __name__ == "__main__":
    main()
