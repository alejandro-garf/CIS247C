# List Append Pop with Loop

import random

deck = [str(i) for i in range(2, 11)] + ['J', 'Q', 'K', 'A']


deck *= 4 #Multiplies all the cards by 4, ignore Suit
print("Number of cards in the deck: ", len(deck))
print(deck)



