def bubbleSort(A):
    arraySorted = False

    while not arraySorted:
        arraySorted = True
        for i in range(len(A) - 1):
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
                arraySorted = False
    return A


if __name__ == '__main__':
    print(bubbleSort([64, 34, 25, 12, 22, 11, 90]))
