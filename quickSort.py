import time
import random

def partition(array, low, high):
    pivot_index = random.randint(low, high)
    array[high], array[pivot_index] = array[pivot_index], array[high]
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1

def quick_sort_iterative(arr):
    stack = [(0, len(arr) - 1)]

    while stack:
        low, high = stack.pop()
        if low < high:
            pivot_index = partition(arr, low, high)
            stack.append((low, pivot_index - 1))
            stack.append((pivot_index + 1, high))

    return arr

def quick_sort(arr):
    n = len(arr)
    start_time = time.time()
    sorted_arr = quick_sort_iterative(arr.copy())
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"For N = {n}, it takes: {elapsed_time:.6f} seconds")
    return sorted_arr
