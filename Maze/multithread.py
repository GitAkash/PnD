import threading
import time

from maze_env import *
import numpy as np

def wayout():
    def leftfollow(env, stop_flag, lock):
        """Solve the algorithm"""
        loc, done = env.reset()
        path = np.array([loc])
        move = 0
        while not done and not stop_flag.is_set():
            with lock:
                availableActions = np.array(env.action_space())
                actions = (availableActions - move) % 4  # Shift actions to relative directions.
                if 3 in actions:
                    move = (3 + move) % 4
                else:
                    if 0 in actions:
                        move = (0 + move) % 4
                    else:
                        move = (1 + move) % 4
                loc, done = env.step(move)
                path = np.vstack((loc, path))

        unique_rows, unique_indices, counts = np.unique(path, axis=0, return_index=True, return_counts=True)

        for i, count in enumerate(counts):
            if count >= 2:
                duplicate_indices = np.where(np.all(path == unique_rows[i], axis=1))[0]

                if duplicate_indices.size >= 2:
                    start_index = duplicate_indices[0]
                    end_index = duplicate_indices[-1]
                    path = np.vstack((path[:start_index + 1, :], path[end_index:, :]))

        stop_flag.set()  # Set the flag when the path is found
        return path

    def rightfollow(env, stop_flag, lock):
        """Solve the algorithm"""
        loc, done = env.reset()
        path = np.array([loc])
        move = 0
        while not done and not stop_flag.is_set():
            with lock:
                availableActions = np.array(env.action_space())
                actions = (availableActions - move) % 4  # Shift actions to relative directions.
                if 1 in actions:
                    move = (1 + move) % 4
                else:
                    if 0 in actions:
                        move = (0 + move) % 4
                    else:
                        move = (3 + move) % 4
                loc, done = env.step(move)
                path = np.vstack((loc, path))

        unique_rows, unique_indices, counts = np.unique(path, axis=0, return_index=True, return_counts=True)
        for i, count in enumerate(counts):
            if count >= 2:
                duplicate_indices = np.where(np.all(path == unique_rows[i], axis=1))[0]

                if duplicate_indices.size >= 2:
                    start_index = duplicate_indices[0]
                    end_index = duplicate_indices[-1]
                    path = np.vstack((path[:start_index + 1, :], path[end_index:, :]))

        stop_flag.set()  # Set the flag when the path is found
        return path

    def leftfollow_thread(env, stop_flag, lock):
        leftfollow(env, stop_flag, lock)

    def rightfollow_thread(env, stop_flag, lock):
        rightfollow(env, stop_flag, lock)

    def main():
        env = make(size=101)

        # Create threading.Event() as a stop flag
        stop_flag = threading.Event()

        # Create a threading.Lock() to control access to the environment
        lock = threading.Lock()

        # Create threads for leftfollow and rightfollow
        left_thread = threading.Thread(target=leftfollow_thread, args=(env, stop_flag, lock))
        right_thread = threading.Thread(target=rightfollow_thread, args=(env, stop_flag, lock))

        # Start the threads
        left_thread.start()
        right_thread.start()

        # Wait for either thread to finish
        left_thread.join()
        right_thread.join()



    if __name__ == '__main__':
        start = time.time()
        main()
        stop = time.time()
        print(stop-start)