import random
import time
import matplotlib.pyplot as plt


def partition(arr, low, high):
    pivot = arr[high]
    i = low

    for j in range(low, high):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[high] = arr[high], arr[i]
    return i


def quickSort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quickSort(arr, low, pivot - 1)
        quickSort(arr, pivot + 1, high)


def get_time(list_sizes):
    random_array = [random.randint(0, list_sizes + 1) for _ in range(list_sizes)]

    start_time = time.time()
    quickSort(random_array, 0, len(random_array) - 1)
    end_time = time.time()
    execution_time = end_time - start_time

    return execution_time


if __name__ == "__main__":
    list_sizes = [10_000, 50_000, 100_000, 500_000, 1_000_000]
    execution_times = {}

    for size in list_sizes:
        time_taken = get_time(size)
        execution_times[size] = time_taken

    for array_size, time_taken in execution_times.items():
        print(f"array of size {array_size} took {time_taken} seconds")



