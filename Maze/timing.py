import csv
from maze_env import *
import numpy as np
import time
from concurrent.futures import ProcessPoolExecutor
import matplotlib.pyplot as plt

def ask():
    start = int(input("Start Size: "))
    end = int(input("End Size: "))
    step = int(input("Step: "))
    num_trials = int(input("Number of Trials: "))

    if start % 2 == 0:
        start += 1
        print("Your starting size must be odd.")

    if step % 2 != 0:
        step += 1
        print("Your step size must be even.")

    if start <= 5:
        print("Your start size must be larger than 5.")
        return None

    if end < start:
        print("The end size must be bigger than the start size.")
        return None

    if step > end - start:
        print("Your step can't be bigger than your searching size.")
        return None

    return start, end, step, num_trials

def time_single(size, num_trials):
    total_time = 0
    for _ in range(num_trials):
        env = make(size=size)
        start_time = time.perf_counter()
        way_out(env)
        end_time = time.perf_counter()
        total_time += end_time - start_time
    average_time = total_time / num_trials
    print(f"Trials: {num_trials}, Size: {size}, Average Time: {average_time} seconds")
    return size, average_time

def times(start, end, step, num_trials):
    sizes = list(range(start, end, step))

    size_and_times = []

    with ProcessPoolExecutor() as executor:
        futures = [executor.submit(time_single, size, num_trials) for size in sizes]

        for future in futures:
            size, average_time = future.result()
            size_and_times.append((size, average_time))

    with open('performance_results.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Size', 'Average Time'])
        csv_writer.writerows(size_and_times)

    sizes, average_times = zip(*size_and_times)

    plt.plot(sizes, average_times, marker='o')
    plt.title('Performance vs. Maze Size')
    plt.xlabel('Maze Size')
    plt.ylabel('Average Time (seconds)')
    plt.savefig('performance_plot.png')
    plt.show()

def way_out(env):
    loc, done = env.reset()
    path = np.array([loc])
    move = 0
    while not done:
        availableActions = np.array(env.action_space())
        actions = (availableActions - move) % 4
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
    return path

def main():
    inputs = ask()
    if inputs is not None:
        start, end, step, num_trials = inputs
        times(start=start, end=end, step=step, num_trials=num_trials)
    else:
        print("Invalid inputs. Exiting.")

if __name__ == '__main__':
    main()
