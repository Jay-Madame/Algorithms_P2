import random
import time
from bubbleSort import *

def getUserLogic():
    userInput =input("Select a sorting algorithm (1-5): ")
    return userInput

def retryLogic(userInput):
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

def sortLogic(intType, typeOfSort):
    ## create array sizes
    testcase1 = [0] * 100
    testcase2 = [0] * 1000
    testcase3 = [0] * 10000
    print(f"""\nCase Scenarios for {typeOfSort} Sort
---------------
1. Best Case
2. Average Case
3. Worst Case
4. Exit {typeOfSort} sort test""")
    caseType = input("Select the case (1-4):")
    match intType:
        case "1":
            match caseType:
                case "1":
                    print("\nIn the best case,")
                    # N = 100
                    start_time = time.time()
                    bubble_sort(createBestCase(testcase1))
                    end_time = time.time()
                    elapsed_time = end_time - start_time
                    print(f"For N = 100, it takes: {elapsed_time:.4f} seconds")

                    # N = 1000
                    start_time = time.time()
                    bubble_sort(createBestCase(testcase2))
                    end_time = time.time()
                    elapsed_time = end_time-start_time
                    print(f"For N = 1000, it takes: {elapsed_time:.4f} seconds")

                    # N = 10000
                    start_time = time.time()
                    bubble_sort(createBestCase(testcase3))
                    end_time = time.time()
                    elapsed_time = end_time-start_time
                    print(f"For N = 10000, it takes: {elapsed_time:.4f} seconds")

                    continueTesting = input("Do you want to input another N (Y/N)? ")
                    continueTesting = continueTesting.upper()
                    if continueTesting == "Y":
                        newArrSize = input("What is the N? ")
                        newArrSizeInt = int(newArrSize)
                        newTestArr = [0] * newArrSizeInt
                        start_time = time.time()
                        bubble_sort(createBestCase(newTestArr))
                        print(f"For N = {newArrSize}, it takes: {elapsed_time:.4f} seconds\n")
                    mainLogic()
                case "2":
                    print("\nIn the average case,")
                    # N = 100
                    start_time = time.time()
                    bubble_sort(createAvgCase(testcase1))
                    end_time = time.time()
                    elapsed_time = end_time - start_time
                    print(f"For N = 100, it takes: {elapsed_time:.4f} seconds")

                    # N = 1000
                    start_time = time.time()
                    bubble_sort(createAvgCase(testcase2))
                    end_time = time.time()
                    elapsed_time = end_time-start_time
                    print(f"For N = 1000, it takes: {elapsed_time:.4f} seconds")

                    # N = 10000
                    start_time = time.time()
                    bubble_sort(createAvgCase(testcase3))
                    end_time = time.time()
                    elapsed_time = end_time-start_time
                    print(f"For N = 10000, it takes: {elapsed_time:.4f} seconds")

                    continueTesting = input("Do you want to input another N (Y/N)? ")
                    continueTesting = continueTesting.upper()
                    if continueTesting == "Y":
                        newArrSize = input("What is the N? ")
                        newArrSizeInt = int(newArrSize)
                        newTestArr = [0] * newArrSizeInt
                        start_time = time.time()
                        bubble_sort(createAvgCase(newTestArr))
                        print(f"For N = {newArrSize}, it takes: {elapsed_time:.4f} seconds\n")
                    mainLogic()
                case "3":
                    print("\nIn the worst case,")
                    # N = 100
                    start_time = time.time()
                    bubble_sort(createWorseCase(testcase1))
                    end_time = time.time()
                    elapsed_time = end_time - start_time
                    print(f"For N = 100, it takes: {elapsed_time:.4f} seconds")

                    # N = 1000
                    start_time = time.time()
                    bubble_sort(createWorseCase(testcase2))
                    end_time = time.time()
                    elapsed_time = end_time-start_time
                    print(f"For N = 1000, it takes: {elapsed_time:.4f} seconds")

                    # N = 10000
                    start_time = time.time()
                    bubble_sort(createWorseCase(testcase3))
                    end_time = time.time()
                    elapsed_time = end_time-start_time
                    print(f"For N = 10000, it takes: {elapsed_time:.4f} seconds")

                    continueTesting = input("Do you want to input another N (Y/N)? ")
                    continueTesting = continueTesting.upper()
                    if continueTesting == "Y":
                        newArrSize = input("What is the N? ")
                        newArrSizeInt = int(newArrSize)
                        newTestArr = [0] * newArrSizeInt
                        start_time = time.time()
                        bubble_sort(createWorseCase(newTestArr))
                        print(f"For N = {newArrSize}, it takes: {elapsed_time:.4f} seconds\n")
                    mainLogic()

                    
                    
                    
def createBestCase(arr):
    for i in range(len(arr)):
        arr[i] = i
    return arr            

def createWorseCase(arr):
    for i in range(len(arr)):
        arr[i] = random.randint(0,50)    
    return arr

def createAvgCase(arr):
    middleRange = len(arr) // 2
    for i in range(middleRange):
        arr[i] = random.randint(0, 50)
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
            print("Please enter a valid statement ")
            userInput = getUserLogic()
            retryLogic(userInput)


mainLogic()
## Bubble Sort

## Merge Sort

## Quick Sort

## Extra Sort