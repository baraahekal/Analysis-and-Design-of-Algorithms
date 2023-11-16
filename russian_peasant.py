def russian(n, m):
    if n == 1:
        return m
    return russian(n // 2, 1) * 2 * m if n % 2 == 0 else russian((n - 1) // 2, 1) * 2 * m + m

print(russian(3,7))
