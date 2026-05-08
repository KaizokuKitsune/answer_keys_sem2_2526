# Alex W.
# Period: 6 & 7
# Week 5 - String Methods
# Method: split
# Time: 10 minutes tops

'''
You have been tasked with creating a random choice selector by your friends.
Your friends want to be able to just type a list of things in all at once and for
it to spit out a random choice from that list'''

import random

choices = input('''Enter the choices (sepearate options by a ','): ''')
choices_list = choices.split(',')
chosen = random.choice(choices_list)

print(f'I have chosen the following option: {chosen}!')