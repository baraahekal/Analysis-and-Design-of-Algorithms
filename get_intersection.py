def get_intersection(lst1, lst2):
    intersection = []

    n, m = len(lst1), len(lst2)
    for i in range(0, n):
        for j in range(m - 1, -1, -1):
            if lst1[i] == lst2[j]:
                intersection.append(lst2[j])
                del lst2[j]
                break

    return intersection


if __name__ == '__main__':
    lst1 = [2, 5, 5, 5]
    lst2 = [2, 2, 2, 3, 5, 5, 7]

    print(get_intersection(lst1, lst2))

