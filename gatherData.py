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

print("Bubble Sort: ")

print("Best Case:")
for i in range(testCases):
    elapsed_time = bubble_sort(createBestCase(testcase1), isTesting)
    print(f"{elapsed_time:.6f}")

print("Worst Case:")
for i in range(testCases):
    elapsed_time = bubble_sort(createWorseCase(testcase1), isTesting)
    print(f"{elapsed_time:.6f}")

print("Average Case:")

for i in range(testCases):
    elapsed_time = bubble_sort(createAvgCase(testcase1), isTesting)
    print(f"{elapsed_time:.6f}")
