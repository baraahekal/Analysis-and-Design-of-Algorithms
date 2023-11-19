def gen_permutations(arr, n):
    if n == 1:
        return [[arr[0]]]

    permutations = []

    for i in range(n):
       
        first_elem = arr[i]
        for perm in gen_permutations(arr[:i] + arr[i+1:], n-1):
            permutations.append([first_elem] + perm)

    return permutations



elements = [1, 2, 3]
print(gen_permutations(elements, len(elements)))

