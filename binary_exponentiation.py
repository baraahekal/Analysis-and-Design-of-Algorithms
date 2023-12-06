def bin_pow(base, exp):
    res = 1
    while exp:
        if exp & 1:
            res *= base
        base *= base
        exp >>= 1
    return res


print(bin_pow(2, 5))
