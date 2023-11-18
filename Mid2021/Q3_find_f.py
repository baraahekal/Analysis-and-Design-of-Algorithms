def find_f(A, i) -> int:
    if i == -1:
        return -1
    if A[i] == i:
        return i
    return find_f(A, i - 1)


A = [0, 2, 3, 4, 5]
print(find_f(A, len(A) - 1))

"""
Time Complexity:
Setting up the recurrence: 
T(n) = T(n-1) + 1, T(0) = 1
     = T(n-2) + 2
     = T(n-3) + 3
     = T(n-k) + k -> solve n = k
     = T(n-n) + n
     = T(0) + n
     = 1 + n
     ∈OO(n)                  
"""
