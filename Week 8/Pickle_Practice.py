# Alex W.
# Period: 6 & 7
# Week 8 - Pickle Practice
# Time: 5 minutes

# get pickle
import pickle

# have user input sets
set1 = set(input('Enter a series of values seperated by commas: ').split(","))
set2 = set(input('Again: ').split(","))

# union sets
unioned_set = set1 | set2

# write to dat file
with open("Week 8/Output File/practice.dat","wb") as outfile:
    pickle.dump(unioned_set,outfile)
    