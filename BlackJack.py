# List Append Pop with Loop

import random

deck = [] #defines a list

for i in range(2, 11): #This will make it go from 2 to 10 just like a deck of cards
    deck.append(str(i)) #Adds a string to the list, needs to be string cause will be adding cards like "jacks" "Kings" etc.
deck.append('J')
deck.append('Q')
deck.append('K')
deck.append('A')

deck *= 4 #Multiplies all the cards by 4, ignore Suit
print("Number of cards in the deck: ", len(deck))
print(deck)

random.shuffle(deck)
print(deck)

top_card = deck.pop(0)
print(top_card)

print(deck)


