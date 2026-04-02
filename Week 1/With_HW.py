# Alex W.
# Period: 6 & 7
# Week 1 - With HW
# Time Spent: 


# V1
days = int(input("Enter the number of days you wish to track the steps for: ")) # Get number of days from user
steps_file = open("steps.txt","w") # open a text file in write mode
for day in range(1,days+1): # for loop to iterate upon user input, use range 1 to input + 1 b/c I want the message to contain the day number
  steps = input(f'''Day #{day} | How many steps did you take? ''') # get input for steps taken on day, uses f string to include day number
  steps_file.write(f'{steps}\n') # use f string for easy/clean writing of value with newline character (\n)
steps_file.close() # close the file for no mem leaks/other errors from leaving file open
  
  
