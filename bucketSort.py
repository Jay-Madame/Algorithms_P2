import time

def insertion_sort(bucket):
    for i in range(1, len(bucket)):
        key = bucket[i]
        j = i - 1
        while j >= 0 and bucket[j] > key:
            bucket[j + 1] = bucket[j]
            j -= 1
        bucket[j + 1] = key

def printTime(elapsed_time, n):
    print(f"For N = {n}, it takes: {elapsed_time:.6f} seconds")


def bucket_sort(arr, isTesting):
    n = len(arr)
    start_time = time.time()
    buckets = [[] for _ in range(n)]

    max_value = max(arr) if arr else 1 
    for num in arr:
        bi = int(num * (n - 1) / max_value)
        buckets[bi].append(num)

    for bucket in buckets:
        insertion_sort(bucket)

    index = 0
    for bucket in buckets:
        for num in bucket:
            arr[index] = num
            index += 1

    end_time = time.time()
    elapsed_time = end_time - start_time
    if (isTesting == False):
        printTime(elapsed_time, n)
    else:
        return elapsed_time
