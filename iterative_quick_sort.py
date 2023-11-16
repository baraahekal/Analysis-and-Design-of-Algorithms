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
    stack = [(low, high)] # creating a stack with initial values low and high

    while stack:
        low, high = stack.pop()

        if low < high:
            pivot = partition(arr, low, high)

            stack.append((low, pivot - 1))
            stack.append((pivot + 1, high))


if __name__ == '__main__':
    arr = [1, 8, 3, 2, 5, 10, 7]
    quickSort(arr, 0, len(arr) - 1)
    print(arr)

