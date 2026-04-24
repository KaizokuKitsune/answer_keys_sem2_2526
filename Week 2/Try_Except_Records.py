# Alex W.
# Period: 6 & 7
# Week 2 - Try/Except and Records
# Time: 1:30 with a LOT of doomscrolling on the side

operation = None # Initialize a variable for the loop

while operation not in ("+","-","*","/"): # input validation 
    operation  = input("What operation would you like to perform? (+,-,*,/) ")

while True: # more input validation with try and except
    try:    
        num1 = float(input("What is the first number? "))
        num2 = float(input("What is the second number? "))
        if num2 == 0 and operation == "/": # divide by zero protection
            print("Can't divide by zero.")
            continue
    except ValueError: # specific error message if value error
        print("Invalid value entered, try again")
    except: # general error message
        print("I don't even know what you did, but it broke something. Please try a normal value.") # Error message with sass
    else: # this executes only if no errors are detected and breaks the while loop, this makes it so that theoretically only valid inputs make it out
        break 

try: # try handler for a secondary divide by zero protection
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        result = num1 / num2
    else:
        print("Interesting")
except ZeroDivisionError: # just in case
    print("Don't even know how you made it this far, but you can't divide by zero.")
except:
    print("An error has occured.")
else:
    print(f"{num1} {operation} {num2} = {result}")
    with open("Week 2/outfile.txt","a") as outfile: # creates record in outfile
        outfile.write(f'Operation: {operation}\n')
        outfile.write(f'Number 1: {num1}\n')
        outfile.write(f'Number 2: {num2}\n')
        outfile.write(f'Result: {result}\n')