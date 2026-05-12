import pickle

with open("Week 8/Output File/practice.dat","rb") as infile:
    print(pickle.load(infile))