import time

def merge_sort(arr):
    n = len(arr)
    start_time = time.time()
    sorted_arr = merge_sort_untimed(arr)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"For N = {n}, it takes: {elapsed_time:.6f} seconds")
    return sorted_arr

def merge_sort_untimed(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort_untimed(arr[:mid])
    right = merge_sort_untimed(arr[mid:])
    return merge(left, right, arr.copy())

def merge(left, right, merged):
    left_cursor, right_cursor = 0, 0

    while left_cursor < len(left) and right_cursor < len(right):
        if left[left_cursor] <= right[right_cursor]:
            merged[left_cursor + right_cursor] = left[left_cursor]
            left_cursor += 1
        else:
            merged[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1

    for left_cursor in range(left_cursor, len(left)):
        merged[left_cursor + right_cursor] = left[left_cursor]

    for right_cursor in range(right_cursor, len(right)):
        merged[left_cursor + right_cursor] = right[right_cursor]

    return merged
