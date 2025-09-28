import time

def bubble_sort(arr):
    n = len(arr)
    start_time = time.time()
    for i in range(n - 1):
        swapped = False  

        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True 

        if not swapped:
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f"For N = {n}, it takes: {elapsed_time:.6f} seconds")
            break
    return arr