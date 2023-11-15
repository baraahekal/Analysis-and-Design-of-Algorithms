# Algorithm  Explanation: https://youtu.be/3GD-3UZGsVI?si=w5QJftnBPlYnqJBb

def max_sub_array_divide_and_conquer(arr, low, hi):
    if low == hi:
        return arr[low]

    mid = (low + hi) // 2
    lss = max_sub_array_divide_and_conquer(arr, low, mid)
    rss = max_sub_array_divide_and_conquer(arr, mid + 1, hi)
    css = max_crossing_sub_array(arr, low, mid, hi)

    return max(lss, rss, css)


def max_crossing_sub_array(arr, low, mid, hi):
    left_sum = -0x3f3f3f3f
    sum = 0

    for i in range(mid, low - 1, -1):
        sum += arr[i]
        left_sum = max(left_sum, sum)

    right_sum = -0x3f3f3f3f
    sum = 0

    for i in range(mid + 1, hi + 1):
        sum += arr[i]
        right_sum = max(right_sum, sum)

    return right_sum + left_sum


if __name__ == '__main__':
    arr_test = [-2, 2, -1, 6, -5]
    print(max_sub_array_divide_and_conquer(arr_test, 0, len(arr_test) - 1))

"""
T(𝑛) = 2¹ T(𝑛 / 2¹) + 1𝑛
     = 2² T(𝑛 / 2²) + 2𝑛
     = 2³ T(𝑛 / 2³) + 3𝑛
     = 2ᵈ T(𝑛 / 2ᵈ) + d𝑛
     = 2^(log(𝑛)) T(𝑛 / 2^(log(𝑛))) + log(n) n
     = 𝑛 T(𝑛 / 𝑛) + 𝑛 log(𝑛)
     = 𝑛 log(𝑛)
     ∈ O(𝑛 log(𝑛))  
"""


