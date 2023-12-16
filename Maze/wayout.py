import csv

from maze_env import *
import numpy as np
import time

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


def times(start, end, step, num_trials):
    sizes = list(range(start, end, step))

    size_and_times = []

    for size in sizes:
        total_time = 0
        for _ in range(num_trials):
            env = make(size=size)

            start_time = time.perf_counter()
            way_out(env)
            end_time = time.perf_counter()

            total_time += end_time - start_time

        average_time = total_time / num_trials
        size_and_times.append((size, average_time))
        print(f"Trials: {num_trials}, Size: {size}, Average Time: {average_time} seconds")

    # Write results to CSV
    with open('performance_results.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Size', 'Average Time'])
        csv_writer.writerows(size_and_times)

    # Plot the results
    sizes, average_times = zip(*size_and_times)

    plt.plot(sizes, average_times, marker='o')
    plt.title('Performance vs. Maze Size')
    plt.xlabel('Maze Size')
    plt.ylabel('Average Time (seconds)')
    plt.savefig('performance_plot.png')
    plt.show()

def main():
    times(start=101, end=301, step=2, num_trials=101)
    # way_out(env)

if __name__ == '__main__':
    main()
