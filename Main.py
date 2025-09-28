import random
from bucketSort import *
from bubbleSort import *
from mergeSort import *
from quickSort import *

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
            sortLogic(userInput, "Bucket")
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
    caseType = input("Select the case (1-4): ")
    isTesting = False
    match intType:
        case "1":
            match caseType:
                case "1":
                    print("\nIn the best case,")
                    bubble_sort(createBestCase(testcase1), isTesting)
                    bubble_sort(createBestCase(testcase2), isTesting)
                    bubble_sort(createBestCase(testcase3), isTesting)
                    
                    continueTesting = input("Do you want to input another N (Y/N)? ")
                    continueTesting = continueTesting.upper()
                    if continueTesting == "Y":
                        newArrSize = input("What is the N? ")
                        newArrSizeInt = int(newArrSize)
                        newTestArr = [0] * newArrSizeInt
                        bubble_sort(createBestCase(newTestArr), isTesting)
                    print("")
                    mainLogic()
                case "2":
                    print("\nIn the average case,")
                    bubble_sort(createAvgCase(testcase1), isTesting)
                    bubble_sort(createAvgCase(testcase2), isTesting)
                    bubble_sort(createAvgCase(testcase3), isTesting)

                    continueTesting = input("Do you want to input another N (Y/N)? ")
                    continueTesting = continueTesting.upper()
                    if continueTesting == "Y":
                        newArrSize = input("What is the N? ")
                        newArrSizeInt = int(newArrSize)
                        newTestArr = [0] * newArrSizeInt
                        bubble_sort(createAvgCase(newTestArr), isTesting)
                    print("")
                    mainLogic()
                case "3":
                    print("\nIn the worst case,")
                    bubble_sort(createWorseCase(testcase1), isTesting)
                    bubble_sort(createWorseCase(testcase2), isTesting)
                    bubble_sort(createWorseCase(testcase3), isTesting)

                    continueTesting = input("Do you want to input another N (Y/N)? ")
                    continueTesting = continueTesting.upper()
                    if continueTesting == "Y":
                        newArrSize = input("What is the N? ")
                        newArrSizeInt = int(newArrSize)
                        newTestArr = [0] * newArrSizeInt
                        bubble_sort(createWorseCase(newTestArr), isTesting)
                    print("")
                    mainLogic()
        case "2":
            match caseType:
                case "1":
                    print("\nIn the best case,")
                    merge_sort(createBestCase(testcase1), isTesting)
                    merge_sort(createBestCase(testcase2), isTesting)
                    merge_sort(createBestCase(testcase3), isTesting)

                    continueTesting = input("Do you want to input another N (Y/N)? ")
                    continueTesting = continueTesting.upper()
                    if continueTesting == "Y":
                        newArrSize = input("What is the N? ")
                        newArrSizeInt = int(newArrSize)
                        newTestArr = [0] * newArrSizeInt
                        merge_sort(createBestCase(newTestArr), isTesting)
                    print("")
                    mainLogic()
                case "2":
                    print("\nIn the average case,")
                    merge_sort(createAvgCase(testcase1), isTesting)
                    merge_sort(createAvgCase(testcase2), isTesting)
                    merge_sort(createAvgCase(testcase3), isTesting)

                    continueTesting = input("Do you want to input another N (Y/N)? ")
                    continueTesting = continueTesting.upper()
                    if continueTesting == "Y":
                        newArrSize = input("What is the N? ")
                        newArrSizeInt = int(newArrSize)
                        newTestArr = [0] * newArrSizeInt
                        merge_sort(createAvgCase(newTestArr), isTesting)
                    print("")
                    mainLogic()
                case "3":
                    print("\nIn the worst case,")
                    merge_sort(createWorseCase(testcase1), isTesting)
                    merge_sort(createWorseCase(testcase2), isTesting)
                    merge_sort(createWorseCase(testcase3), isTesting)

                    continueTesting = input("Do you want to input another N (Y/N)? ")
                    continueTesting = continueTesting.upper()
                    if continueTesting == "Y":
                        newArrSize = input("What is the N? ")
                        newArrSizeInt = int(newArrSize)
                        newTestArr = [0] * newArrSizeInt
                        merge_sort(createWorseCase(newTestArr), isTesting)
                    print("")
                    mainLogic()
        case "3":
            match caseType:
                case "1":
                    print("\nIn the best case,")
                    quick_sort(createBestCase(testcase1), isTesting)
                    quick_sort(createBestCase(testcase2), isTesting)
                    quick_sort(createBestCase(testcase3), isTesting)

                    continueTesting = input("Do you want to input another N (Y/N)? ")
                    continueTesting = continueTesting.upper()
                    if continueTesting == "Y":
                        newArrSize = input("What is the N? ")
                        newArrSizeInt = int(newArrSize)
                        newTestArr = [0] * newArrSizeInt
                        quick_sort(createBestCase(newTestArr), isTesting)
                    print("")
                    mainLogic()
                case "2":
                    print("\nIn the average case,")
                    quick_sort(createAvgCase(testcase1), isTesting)
                    quick_sort(createAvgCase(testcase2), isTesting)
                    quick_sort(createAvgCase(testcase3), isTesting)

                    continueTesting = input("Do you want to input another N (Y/N)? ")
                    continueTesting = continueTesting.upper()
                    if continueTesting == "Y":
                        newArrSize = input("What is the N? ")
                        newArrSizeInt = int(newArrSize)
                        newTestArr = [0] * newArrSizeInt
                        quick_sort(createAvgCase(newTestArr), isTesting)
                    print("")
                    mainLogic()
                case "3":
                    print("\nIn the worst case,")
                    quick_sort(createWorseCase(testcase1), isTesting)
                    quick_sort(createWorseCase(testcase2), isTesting)
                    quick_sort(createWorseCase(testcase3), isTesting)

                    continueTesting = input("Do you want to input another N (Y/N)? ")
                    continueTesting = continueTesting.upper()
                    if continueTesting == "Y":
                        newArrSize = input("What is the N? ")
                        newArrSizeInt = int(newArrSize)
                        newTestArr = [0] * newArrSizeInt
                        quick_sort(createWorseCase(newTestArr), isTesting)
                    print("")
                    mainLogic()
        case "4":
            match caseType:
                case "1":
                    print("\nIn the best case,")
                    bucket_sort(createBestCase(testcase1), isTesting)
                    bucket_sort(createBestCase(testcase2), isTesting)
                    bucket_sort(createBestCase(testcase3), isTesting)

                    continueTesting = input("Do you want to input another N (Y/N)? ")
                    continueTesting = continueTesting.upper()
                    if continueTesting == "Y":
                        newArrSize = input("What is the N? ")
                        newArrSizeInt = int(newArrSize)
                        newTestArr = [0] * newArrSizeInt
                        bucket_sort(createBestCase(newTestArr), isTesting)
                    print("")
                    mainLogic()
                case "2":
                    print("\nIn the average case,")
                    bucket_sort(createAvgCase(testcase1), isTesting)
                    bucket_sort(createAvgCase(testcase2), isTesting)
                    bucket_sort(createAvgCase(testcase3), isTesting)

                    continueTesting = input("Do you want to input another N (Y/N)? ")
                    continueTesting = continueTesting.upper()
                    if continueTesting == "Y":
                        newArrSize = input("What is the N? ")
                        newArrSizeInt = int(newArrSize)
                        newTestArr = [0] * newArrSizeInt
                        bucket_sort(createAvgCase(newTestArr), isTesting)
                    print("")
                    mainLogic()
                case "3":
                    print("\nIn the worst case,")
                    bucket_sort(createWorseCase(testcase1), isTesting)
                    bucket_sort(createWorseCase(testcase2), isTesting)
                    bucket_sort(createWorseCase(testcase3), isTesting)

                    continueTesting = input("Do you want to input another N (Y/N)? ")
                    continueTesting = continueTesting.upper()
                    if continueTesting == "Y":
                        newArrSize = input("What is the N? ")
                        newArrSizeInt = int(newArrSize)
                        newTestArr = [0] * newArrSizeInt
                        bucket_sort(createWorseCase(newTestArr), isTesting)
                    print("")
                    mainLogic()

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

def mainLogic():
    print("""Welcome to the test suite of selected sorting algorithms!
Select the sorting algorithm you want to test.
-------------------------
1. Bubble Sort
2. Merge Sort
3. Quick Sort
4. Bucket Sort
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
            sortLogic(userInput, "Bucket")
        case "5":
            exit
        case _:
            print("Please enter a valid statement ")
            userInput = getUserLogic()
            retryLogic(userInput)

mainLogic()
