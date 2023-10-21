def get_intersection(lst1, lst2):
    intersection = []

    for i in range(len(lst1)):
        for j in range(len(lst2)):
            if lst1[i] == lst2[j]:
                intersection.append(lst2[j])
                del lst2[j]
                break

    return intersection


if __name__ == '__main__':
    lst1 = [2, 5, 5, 5]
    lst2 = [2, 2, 2, 3, 5, 5, 7]

    print(get_intersection(lst1, lst2))
