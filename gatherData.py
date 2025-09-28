import random
import time
from bucketSort import *
from bubbleSort import *
from mergeSort import *
from quickSort import *

def createBestCase(arr):
    for i in range(len(arr)):
        arr[i] = i
    return arr            

def createWorseCase(arr):
    n = len(arr)
    for i in range(n):
        arr[i] = n - 1 - i
    return arr

def createAvgCase(arr):
    for i in range(len(arr)):
        arr[i] = random.randint(0,10000)    
    return arr

## Creating Testing Environment

isTesting = True
testCases = 30
testcase1 = [0] * 100
testcase2 = [0] * 1000
testcase3 = [0] * 10000

print("\n\nNEW DATA \n\n")

print("Best Case:")
for i in range(testCases):
    elapsed_time = bucket_sort(createBestCase(testcase3), isTesting)
    print(f"{elapsed_time:.6f}")

print("\nAverage Case:")

for i in range(testCases):
    elapsed_time = bucket_sort(createAvgCase(testcase3), isTesting)
    print(f"{elapsed_time:.6f}")

print("\nWorst Case:")
for i in range(testCases):
    elapsed_time = bucket_sort(createWorseCase(testcase3), isTesting)
    print(f"{elapsed_time:.6f}")


