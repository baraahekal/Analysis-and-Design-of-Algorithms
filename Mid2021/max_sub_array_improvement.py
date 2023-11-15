# Kadane's Algorithm
# Just for curiosity, out of Midterm question scope

def max_subarray_sum_kadane(arr):
    cur_sum, max_sum = arr[0], arr[0]
    for i in range(1, len(arr)):
        cur_sum = max(cur_sum + arr[i], arr[i])
        max_sum = max(max_sum, cur_sum)
    return max_sum
