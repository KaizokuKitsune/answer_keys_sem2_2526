# Alex W.
# Period: 6 & 7
# Week 8 - Schedule Helper
# Time: 5 minutes

# get user input
times_1 = set(input("Enter the available times for person 1 seperated by commas: ").split(","))
times_2 = set(input("Enter the available times for person 2 seperated by commas: ").split(","))

# find intersection of sets
times = times_1 & times_2
# print
print(f'You can both meet at the following times: {times}')