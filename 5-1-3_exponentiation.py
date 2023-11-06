# 10^16 => 10^8 * 10^8
def fast_pow(base, exponent):
    if not exponent:
        return 1
    else:
        sq = fast_pow(base, exponent >> 1)
        return sq * sq if ~exponent & 1 else sq * sq * base


# 2^5 => 2 * 2^(5-1)
def pow(base, exponent):
    if not exponent:
        return 1
    else:
        return base * pow(base, exponent - 1)


if __name__ == '__main__':
    print(pow(2, 5)) #32
    print(fast_pow(2, 5)) #32

