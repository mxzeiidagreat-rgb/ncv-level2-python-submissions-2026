def getMarks():
    marks = []

    mark = int(input("Enter mark (or -1 to stop): "))

    while mark != -1:
        marks.append(mark)
        mark = int(input("Enter mark (or -1 to stop): "))

    return marks


def printListSize(marks):
    print(f"Our list has {len(marks)} elements")


def printMarks(marks):
    for x in range(len(marks)):
        print(f"Mark {x + 1} is {marks[x]}")


def getSumOfMarks(marks):
    total = 0

    for mark in marks:
        total += mark

    return total


def determineHighest(marks):
    if len(marks) == 0:
        print("No marks entered.")
        return

    highest = marks[0]

    for currentMark in marks:
        if currentMark > highest:
            highest = currentMark

    print(f"The highest mark is {highest}")


menu = "\nEnter 1: Capture marks\n"
menu += "Enter 2: Check number of marks\n"
menu += "Enter 3: Calculate average of marks\n"
menu += "Enter 4: Find highest mark\n"
menu += "Enter -1: Exit\n"

marksEntered = []

print(menu)
choice = int(input("Make your choice: "))

while choice != -1:

    if choice == 1:
        marksEntered = getMarks()
        print(marksEntered)

    elif choice == 2:
        printListSize(marksEntered)

    elif choice == 3:
        if len(marksEntered) > 0:
            calcSum = getSumOfMarks(marksEntered)
            average = calcSum / len(marksEntered)
            print(f"The average mark is {average:.2f}")
        else:
            print("No marks entered.")

    elif choice == 4:
        determineHighest(marksEntered)

    else:
        print("Not on the menu")

    print(menu)
    choice = int(input("Make your choice (-1 to exit): "))

print("Program ended.")