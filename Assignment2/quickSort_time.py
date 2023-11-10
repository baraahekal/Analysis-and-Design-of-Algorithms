import random
import time


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


def compute_time(arr):
    start_time = time.time()
    quickSort(arr, 0, len(arr) - 1)
    end_time = time.time()
    execution_time = end_time - start_time
    return execution_time


if __name__ == '__main__':
    # Generating array of 2 large arrays, each of size 1 million
    array_of_arrays = list([random.sample(range(1, 10000001), 1000000) for _ in range(2)])

    # Generating and adding one sorted list of size 1 million to show the difference between different inputs
    sorted_one = [random.sample(range(1, 10000001), 1000000)]
    sorted_one.sort()
    array_of_arrays.append(sorted_one)

    all_times = []
    for array in array_of_arrays:
        all_times.append(compute_time(array))

    for time in all_times:
        print(time)

