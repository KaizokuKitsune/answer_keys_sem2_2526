# Alex W.
# Period: 6 & 7
# Week 3 - Creating and Editing Lists
# Time: 

edit = ""
ref = -1

while True: # Input Validation 
    try:
        user_inputed_value = int(input("Enter the length of the list: "))
    except Exception as e:
        print(f"Please enter a valid input. Error: {e}")
    else:
        break

# going to use the headstart I gave y'all
i = user_inputed_value
user_list = []
for n in range(1, i+1):
  user_input = input(f'Please enter the value for element {n}: ')
  user_list += [user_input]

print(f'''Your list: {user_list}''')


while edit.lower() != "y" and edit.lower() != "n":
    edit = input("Would you like to change a value? [Y/N] ")

if edit.lower() == "y":
    try:
        while ref not in range(0,user_inputed_value-1):
            ref = int(input(f"Enter the index of the value you wish to edit(0-{user_input_value-1}): "))
            user_list[ref]
    except IndexError:
        print("Invalid Index.")
    except Exception as e:
        print(f"Please enter a valid input. Error: {e}")
    user_list[ref] = input(f"Enter the value to replace {user_list[ref]}: ")
    print(f"Updated List: {user_list}")
else:
    print(f"Final List: {user_list}")
