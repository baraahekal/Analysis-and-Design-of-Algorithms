def partition(arr, low, high):
    pivot = arr[high]
    i = low

    for j in range(low, high):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[high] = arr[high], arr[i]
    return i


def quickSelect(arr, low, high, k):
    if k > len(arr) - 1:
        return 0x3f3f3f3f

    while low < high:
        pivot = partition(arr, low, high)
        if pivot == k:
            return arr[pivot]
        elif pivot > k:
            high = pivot - 1
        else:
            low = pivot + 1

    return arr[k]


if __name__ == '__main__':
    arr = [1, 8, 3, 2, 5, 10, 7]
    print(quickSelect(arr, 0, len(arr) - 1, k=3))
