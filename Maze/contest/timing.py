import csv
import time
from maze_env import *
from concurrent.futures import ProcessPoolExecutor
import matplotlib.pyplot as plt
import numpy as np

def ask():
    start = int(input("Start Size: "))
    end = int(input("End Size: "))
    step = int(input("Step: "))
    num_trials = int(input("Number of Trials: "))

    if start % 2 == 0:
        start += 1
        print("Your starting size must be odd, it got corrected.")

    if step % 2 != 0:
        step += 1
        print("Your step size must be even, it got corrected.")

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

from contestWayOut import way_out

def main():
    inputs = ask()
    if inputs is not None:
        start, end, step, num_trials = inputs
        times(start=start, end=end, step=step, num_trials=num_trials)
    else:
        print("Invalid inputs. Exiting.")

if __name__ == '__main__':
    main()
