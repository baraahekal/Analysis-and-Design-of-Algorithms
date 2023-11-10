def gen_bit_strings_iterative(n):
    bits_string = [""]

    for _ in range(n):
        for i in range(len(bits_string)):
            bits_string.append(bits_string[i] + '1')
            bits_string[i] += '0'

    return bits_string


if __name__ == '__main__':
    print(gen_bit_strings_iterative(3))
