# Recursive DP O(n) instead of O(2ⁿ) using straight forward recursion
def fib_recursive(n):
    global res
    if res[n]:
        return res[n]
    if n <= 2:
        res[n] = 1
    else:
        res[n] = fib_recursive(n - 1) + fib_recursive(n - 2)
    return res[n]


# Iterative DP O(n)
def fib_iterative(n):
    global res
    res[1] = res[2] = 1
    for i in range(3, n + 1):
        res[i] = res[i - 1] + res[i - 2]
    return res[n]


n = int(input())
res = [0] * (n + 1)
print(fib_iterative(n))
print(fib_recursive(n))
