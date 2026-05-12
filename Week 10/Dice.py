# Alex W.
# Period: 6 & 7
# Week 10 - Dice
# Time: 15 minutes


# need this
import random

'''make a dice that takes arguments
your code likely would not take arguments as we hadn't really covered that
so just ignore the 6 passed to it later (I'll comment there too)
and replace 'sides' with 6
'''
class Dice:
    def __init__(self,sides):
        self.__sides = sides
    def roll(self):
        side = random.randint(1,self.__sides)
        print(f'You rolled a {side}!')
        

dice = Dice(6) # create an instance (ignore the 6)
dice.roll() # call the roll function


