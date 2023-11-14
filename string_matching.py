def string_matching(T, P):
    for i in range(len(T) - len(P) + 1):
        idx_word = 0
        while idx_word < len(P) and T[i + idx_word] == P[idx_word]:
            idx_word += 1

        if idx_word == len(P):
            return i
    return -1


print(string_matching("Participating in ICPC is the dream of 2024", "ICPC"))
