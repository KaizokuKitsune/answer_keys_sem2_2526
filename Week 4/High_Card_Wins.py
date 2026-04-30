# Alex W.
# Period: 6 & 7
# Week 4 - High Card Wins
# Time: 

import random # the backbone of this code
# Stealing my own work (again) a good coding practice btw (Deck 3)
# Reformatting so its not so ugly to look at (python cant tell as long as its in parentheses)
Deck = list((s,k,v) 
             for s in ('♠','♥','♣','♦') 
             for k in (2,3,4,5,6,7,8,9,10,'J','Q','K','A') 
             for v in (2,3,4,5,6,7,8,9,10,11,12,13,14) if v == ((2,3,4,5,6,7,8,9,10,'J','Q','K','A').index(k)+2))

random.shuffle(Deck) #Shuffle the Deck
user_hand = []
comp_hand = []

# Deal and Display

for i in range(5): # 5 card hand
    user_hand.append(Deck.pop()) # did it like this to simulate how a deal would actually go, one to me one to you kinda thing
    comp_hand.append(Deck.pop())

# print hand
print(f'Your hand:')
i = 1
for card in user_hand:
    print(f'{i} — {card[1]}{card[0]}') # fun fact: Em-Dash alt code is alt+0151
    i+=1

# Discard Portion
confirm = False
discard = ""
num_dis = 0
dis_cards = []
discard_cards = []
while discard.lower() != "y" and discard.lower() != "n":
    discard = input("Would you like to discard up to 3 cards?")
if discard.lower() == "y":
    print("This will loop if you mess up so do please try and play nice.") # warning because this very rapidly exploded beyond necessary scope
    while True:
        temp_Deck = Deck # to preserve
        temp_hand = user_hand
        try:
            while not confirm:
                dis_cards = []   
                num_dis = 0   
                discard_cards = []          
                while num_dis < 1 or num_dis > 3: # while cards to discard is not between 1 and 3 inclusive
                    num_dis = int(input("How many cards would you like to discard? "))
                for x in range(1,num_dis+1): # for number of cards discarded
                    dis_cards.append(int(input(f"{x} of {num_dis} — Give the number (left of the dash) of the card you wish to discard: ")))
                print("The cards you have selected to discard:")
                for spot in dis_cards: # prints the cards to be discarded for the user to see
                    print(f"{spot} — {temp_hand[spot-1][1]}{temp_hand[spot-1][0]}")
                confirm_q = input('Would you like to confirm your choice(s)?(Y/N) ')
                if confirm_q.lower() == "y": # if user confirms cards
                    confirm = True
                    for spot in dis_cards: # make a container for the cards to be removed
                        discard_cards.append(temp_hand[spot-1])
                    for card in discard_cards: # remove cards of values saved
                        temp_hand.remove(card)
                    while len(temp_hand) != 5: # add new cards until hand is full
                        temp_hand.append(temp_Deck.pop())
        except:
            continue # if error restart
        finally:
            user_hand = temp_hand
            Deck = temp_Deck
            print('Your new hand:')
            i = 1
            for card in user_hand:
                print(f'{i} — {card[1]}{card[0]}')
                i+=1
            break
# Play Portion
playstyle = 1
rounds = 3
# the only one required, I might add more
if playstyle == 1: # the default one
    for round in range(rounds):
        user_card = []
        comp_card = comp_hand.pop()
        
