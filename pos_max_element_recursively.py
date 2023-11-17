def pos_max_element(A, low, hi):
    if low == hi:
        return low
    
    mid = (low + hi) // 2
    max_pos_left = pos_max_element(A, low, mid)
    max_pos_right = pos_max_element(A, mid + 1, hi)

    return max_pos_left if A[max_pos_left] > A[max_pos_right] else max_pos_right



# complex simple more time consuming version:
def f(A, low, hi):
    if low == hi: return low
    mid = (low + hi) // 2
    return f(A, low, mid) if A[f(A, low, mid)] > A[f(A, mid + 1, hi)] else f(A, mid + 1, hi)
