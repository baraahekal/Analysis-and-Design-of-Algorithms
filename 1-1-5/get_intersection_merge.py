def get_intersection(lst1, lst2):
    intersection = []

    n, m = len(lst1), len(lst2)
    i, j = 0, 0

    while i < n and j < m:
        if lst1[i] == lst2[j]:
            intersection.append(lst1[i])
            i += 1
            j += 1
        elif lst1[i] < lst2[j]:
            i += 1
        else:
            j += 1

    return intersection


if __name__ == '__main__':
    lst1 = [2, 5, 5, 5]
    lst2 = [2, 2, 2, 3, 5, 5, 7]

    print(get_intersection(lst1, lst2))

