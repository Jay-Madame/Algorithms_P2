import time
import random

def printTime(elapsed_time, n):
    print(f"For N = {n}, it takes: {elapsed_time:.6f} seconds")

# Insertion sort for small arrays
def insertion_sort(arr, low, high):
    for i in range(low + 1, high + 1):
        key = arr[i]
        j = i - 1
        while j >= low and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Median-of-three pivot selection
def median_of_three(arr, low, high):
    mid = (low + high) // 2
    a, b, c = arr[low], arr[mid], arr[high]
    if a > b:
        if b > c:
            return mid
        elif a > c:
            return high
        else:
            return low
    else:
        if a > c:
            return low
        elif b > c:
            return high
        else:
            return mid

# Dutch National Flag (3-way partition)
def three_way_partition(arr, low, high):
    pivot_index = median_of_three(arr, low, high)
    arr[low], arr[pivot_index] = arr[pivot_index], arr[low]
    pivot = arr[low]

    lt = low
    i = low + 1
    gt = high

    while i <= gt:
        if arr[i] < pivot:
            arr[lt], arr[i] = arr[i], arr[lt]
            lt += 1
            i += 1
        elif arr[i] > pivot:
            arr[i], arr[gt] = arr[gt], arr[i]
            gt -= 1
        else:
            i += 1
    return lt, gt

# Optimized quicksort (iterative with insertion sort & 3-way partitioning)
def quick_sort_optimized(arr):
    INSERTION_SORT_THRESHOLD = 16
    stack = [(0, len(arr) - 1)]
    
    while stack:
        low, high = stack.pop()
        if high - low <= INSERTION_SORT_THRESHOLD:
            insertion_sort(arr, low, high)
            continue

        lt, gt = three_way_partition(arr, low, high)

        # Push larger partition first for better stack efficiency
        if lt - low < high - gt:
            if lt > low:
                stack.append((low, lt - 1))
            if gt < high:
                stack.append((gt + 1, high))
        else:
            if gt < high:
                stack.append((gt + 1, high))
            if lt > low:
                stack.append((low, lt - 1))

# Wrapper for timing & integration with main.py
def quick_sort(arr, isTesting):
    start = time.perf_counter()
    quick_sort_optimized(arr)
    end = time.perf_counter()
    elapsed_time = end-start
    if (isTesting == False):
        printTime(elapsed_time, len(arr))
    else:
        return elapsed_time
    return arr
