
from sys import exit as exit # not needed but is nice
import random # is needed for a lot
from mine import input_validate

class Coin:
    def __init__(self):
        self.__side_up = "Heads"
    def flip(self):
        if random.randint(0,1) == 1:
            self.__side_up = "Heads"
            return self.__side_up
        else:
            self.__side_up = "Tails"
            return self.__side_up


class D4:
    def __init__(self,):
        self.__sides = 4
    def roll(self):
        side = random.randint(1,self.__sides)
        return side


class D6:
    def __init__(self,):
        self.__sides = 6
    def roll(self):
        side = random.randint(1,self.__sides)
        return side


class D8:
    def __init__(self,):
        self.__sides = 8
    def roll(self):
        side = random.randint(1,self.__sides)
        return side
    

class D10:
    def __init__(self,):
        self.__sides = 10
    def roll(self):
        side = random.randint(1,self.__sides)
        return side

class D12:
    def __init__(self,):
        self.__sides = 12
    def roll(self):
        side = random.randint(1,self.__sides)
        return side


class D20:
    def __init__(self,):
        self.__sides = 20
    def roll(self):
        side = random.randint(1,self.__sides)
        return side
    

class D100:
    def __init__(self,):
        self.__sides = 100
    def roll(self):
        side = random.randint(1,self.__sides)
        return side

def spells():
    print('Made it to spells')
    main()

def roll_dice():
    dice = None
    print(f'''
1 – Coin
2 – D4
3 – D6
4 – D8
5 – D10
6 – D12
7 – D20
8 – D100
9 – Go Back
''')
    while dice not in ('1','2','3','4','5','6','7','8','9'): dice = input('>>> ')
    if dice != "9":
        num_dice = input_validate(int,"Enter the number of dice you would like to roll: ")
        print(num_dice)
    main()

def main():
    print(f'''
Options:
1 – Roll a Dice
2 – Cast a Spell
3 – Exit
''')
    menu = None
    while menu not in ["1","2","3"]: menu = input('>>> ')
    if menu == "1": roll_dice()
    if menu == "2": spells()
    if menu == "3": exit("Goodbye!")
    
    
main()