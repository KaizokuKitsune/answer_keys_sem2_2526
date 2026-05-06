# Alex W.
# Period: 6 & 7
# Week 3 - Creating and Editing Lists
# Time: 1:15 I made a lot of spelling errors and a couple logic errors - it happens

# initialize variables for later use in while loops
edit = ""
ref = -1

while True: # Input Validation 
    try:
        user_inputted_value = int(input("Enter the length of the list: "))
        if user_inputted_value <= 0: # stops 0 and negative values
            print(f"{user_inputted_value} is not a valid list length.")
            continue
    except Exception as e: # 'Exception as e' will save any exception's message as it is the superclass of all exceptions
        print(f"Please enter a valid input. Error: {e}")
    else:
        break

# going to use the headstart I gave y'all
i = user_inputted_value
user_list = []
for n in range(1, i+1): # iterate accross range of 1 to list length + 1 for use in print statement
  user_input = input(f'Please enter the value for element {n}: ')
  user_list += [user_input]

print(f'''Your list: {user_list}''') # print the original list


while edit.lower() != "y" and edit.lower() != "n": # keep user in loop until valid string input
    edit = input("Would you like to change a value? [Y/N] ")

if edit.lower() == "y": # if edit is yes
    while True: # another input validation + error handle loop 
        try:
            while ref not in range(0,user_inputted_value-1): # should keep the user trapped until a valid input is given
                ref = int(input(f"Enter the index of the value you wish to edit(0-{user_inputted_value-1}): "))
            user_list[ref] # used to trigger index error if the value they entered is wrong should never happen because of while loop though
        except IndexError: # made it a requirement but it should never get here
            print("Invalid Index.")
        except Exception as e: # mainly to handle throwing non int values into ref value
            print(f"Please enter a valid input. Error: {e}")
        else:
            break
    user_list[ref] = input(f"Enter the value to replace {user_list[ref]}: ") # prompts user to enter value and show value to be changed
    print(f"Updated List: {user_list}") # print updated list
else:
    print(f"Final List: {user_list}") # print final list if user doesn't want to change it
