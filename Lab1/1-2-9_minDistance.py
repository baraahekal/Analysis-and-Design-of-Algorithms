def partition(A, l, h):
    pivot = A[l]
    i = l
    j = h

    while True:
        i += 1
        while i < h and A[i] <= pivot:
            i += 1
        while A[j] > pivot:
            j -= 1
        if i < j:
            A[i], A[j] = A[j], A[i]
        else:
            A[l], A[j] = A[j], A[l]
            return j


def quick_sort(A, l, h):
    if l < h:
        pivot = partition(A, l, h)
        quick_sort(A, l, pivot - 1)
        quick_sort(A, pivot + 1, h)


def minDistance(A):
    mn = float('inf')
    quick_sort(A, 0, len(A) - 1)
    
    for i in range(len(A) - 1):
        mn = min(mn, abs(A[i] - A[i + 1]))
        if not mn:
            break

    return mn


if __name__ == "__main__":
    print(minDistance([1, 5, -2, 3, 7, 10, 1]))

