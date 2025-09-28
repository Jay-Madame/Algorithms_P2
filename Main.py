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


mainLogic()
## Bubble Sort

## Merge Sort

## Quick Sort

## Extra Sort