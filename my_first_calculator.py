# My first Calculator

''' This is Python program for simple calculator which can do addition, 
subtraction, multiplication, division, square root and cube '''

# defined variables
operation = int(input("Please select operation:\n" 
                "Type 1 for addition\n" 
                "Type 2 for subtraction\n"
                "Type 3 for multiplication\n"
                "Type 4 for division\n"
                "Type 5 for square\n" 
                "Type 6 for cube \n"))

a = int(input("Please select first number : "))
b = int(input("Please select second number : "))

add = a + b
subtract = a - b
multiply = a * b
divide = a / b
square = a ** 2
cube = a ** 3

# Function to do calculation
def calc():
    # addition
    if operation == 1: 
        print(a, " + ", b, " = ", add)
    # subtraction
    elif operation == 2: 
        print(a, " - ", b, " = ", subtract)
    # multiplication
    elif operation == 3: 
        print(a, " x ", b, " = ", multiply)
    # division
    elif operation == 4:
        print(a, " / ", b, " = ", divide)
    # square root
    elif operation == 5:
        print(a, " ^2 ", b, " = ", square)
    # cube
    elif operation == 6:
        print(a, " ^3 ", b, " = ", cube)

    else:
        print("Invalid input")

calc()   

