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


def is_anagram(word1, word2):
    if len(word1) != len(word2):
        return False

    word1_lst = list(word1)
    word2_lst = list(word2)

    quick_sort(word1_lst, 0, len(word1_lst) - 1)
    quick_sort(word2_lst, 0, len(word2_lst) - 1)

    return word1_lst == word2_lst


if __name__ == "__main__":
    print(is_anagram("tea", "eat"))

