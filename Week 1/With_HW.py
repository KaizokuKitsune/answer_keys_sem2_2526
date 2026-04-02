# Alex W.
# Period: 6 & 7
# Week 1 - With HW
# Time Spent: 


# Part 1
days = int(input("Enter the number of days you wish to track the steps for: ")) # Get number of days from user
steps_file = open("Week 1/steps.txt","w") # open a text file in write mode, needed to specify a file path of "Week 1/" to get it to be created in the file directory correctly
for day in range(1,days+1): # for loop to iterate upon user input, use range 1 to input + 1 b/c I want the message to contain the day number
  steps = input(f'''Day #{day} | How many steps did you take? ''') # get input for steps taken on day, uses f string to include day number
  steps_file.write(f'{steps}\n') # use f string for easy/clean writing of value with newline character (\n)
steps_file.close() # close the file for no mem leaks/other errors from leaving file open
  
  
# Part 2
steps_file = open("Week 1/steps.txt","r") # opens the file in read mode
read_day = steps_file.readline() # reads the first line of the step file
total_steps = 0 # initializes a sum value
while read_day != '': # While line is not blank
  total_steps += int(read_day) # converts the line to int and adds it to the sum
  read_day = steps_file.readline()
print(f'''The total steps tracked is {total_steps}''')