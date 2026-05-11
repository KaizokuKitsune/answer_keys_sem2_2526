# Alex W.
# Period: 6 & 7
# Week 7 - Dictionaries
# Time: 25 minutes

# initialize dictionary
bds = {}

def add_bds():
    # get num of people
    num_bds = int(input('Enter the number of birthdays you wish to add: '))
    # add people
    for x in range(num_bds):
        bd_name = input("Enter the person's name: ")
        global bds
        bds[bd_name] = input("Enter the person's birthday:")

# funciton to list bds
def list_bds():
    global bds
    for key in bds:
        print(bds[key])

# function to list people
def list_people():
    global bds
    for key in bds:
        print(key)
        


# set selection = to 1 so that user has to add bds before anything
selection = 1

while True:
    if selection == 1:
        add_bds()
    elif selection == 2:
        list_people()
    elif selection == 3:
        list_bds()
    elif selection == 4:
        bds.clear()
    elif selection == 5:
        break
    else:
        continue
    print(f'''Options:
1 – Add Birthdays
2 – List People
3 – List Birthdays
4 – Clear
5 – Exit
''')
    selection = int(input('Option: '))