def pos_max_element(A, low, hi):
    if low == hi:
        return low
    
    mid = (low + hi) // 2
    max_pos_left = pos_max_element(A, low, mid)
    max_pos_right = pos_max_element(A, mid + 1, hi)

    return max_pos_left if A[max_pos_left] > A[max_pos_right] else max_pos_right
