import random
import time
from bubbleSort import *

def getUserLogic():
    userInput =input("Select a sorting algorithm (1-5):")
    return userInput

def retryLogic(userInput):
    match userInput:
        case "1":
            print("Need to implement")
        case "2":
            print("Need to implement")
        case "3":
            print("Need to implement")
        case "4":
            print("Need to implement")
        case "5":
            exit
        case _:
            print("Please enter a valid statement")
            userInput = getUserLogic()
            retryLogic(userInput)

def sortLogic(intType, typeOfSort):
    ## create array sizes
    testcase1 = [0] * 100
    testcase2 = [0] * 1000
    testcase3 = [0] * 10000
    print(f"""Case Scenarios for {typeOfSort} Sort
---------------
1. Best Case
2. Average Case
3. Worst Case
4. Exit {typeOfSort} sort test""")
    caseType = input("Select the case (1-4):")
    match caseType:
        case "1":
            match intType:
                case "1":
                    print("In the best case,")
                    # N = 100
                    start_time = time.time()
                    bubble_sort(testcase1)
                    end_time = time.time()
                    elapsed_time = end_time - start_time
                    print(f"For N = 100, it takes: {elapsed_time:.4f} seconds")

                    # N = 1000
                    start_time = time.time()
                    bubble_sort(testcase2)
                    end_time = time.time()
                    elapsed_time = end_time-start_time
                    print(f"For N = 1000, it takes: {elapsed_time:.4f} seconds")

                    # N = 10000
                    start_time = time.time()
                    bubble_sort(testcase3)
                    end_time = time.time()
                    elapsed_time = end_time-start_time
                    print(f"For N = 10000, it takes: {elapsed_time:.4f} seconds")
                    
            

def createWorseCase(arr):
    for i in arr:
        arr[i] = random.randint(0,50)    
    return arr

def createAvgCase(arr):
    middleRange = len(arr)
    for i in middleRange:
        arr[i] = random.randint(0,50)
    return arr


def mainLogic():
    print("""Welcome to the test suite of selected sorting algorithms!
Select the sorting algorithm you want to test.
-------------------------
1. Bubble Sort
2. Merge Sort
3. Quick Sort
4. Heap Sort (replacing this line with the algorithm you choose)
5. Exit""")
    userInput = getUserLogic();

    match userInput:
        case "1":
            sortLogic(userInput, "Bubble")
        case "2":
            sortLogic(userInput, "Merge")
        case "3":
            sortLogic(userInput, "Quick")
        case "4":
            sortLogic(userInput, "Heap")
        case "5":
            exit
        case _:
            print("Please enter a valid statement")
            userInput = getUserLogic()
            retryLogic(userInput)


mainLogic()
## Bubble Sort

## Merge Sort

## Quick Sort

## Extra Sort