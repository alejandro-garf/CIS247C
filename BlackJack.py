# Function Calls, Parametere and Return

import random

def initialize_deck():
    deck = [str(i) for i in range(2, 11)] + ['J', 'Q', 'K', 'A']
    deck *= 4 #Multiplies all the cards by 4, ignore Suit
    random.shuffle(deck)
    return deck

def draw_card(deck):
    card = deck.pop()
    return card

def card_value(card):
    if card in ['J', 'Q', 'K']:
        return 10
    elif card == 'A':
        return 11
    else:
        return int(card)

def calculate_hand(hand):
    value = 0;
    for card in hand: #loops through every card in the hand
        value += card_value(card)

    if value > 21 and 'A' in hand:
        value -= 10

    return value


def main():
    card_deck = initialize_deck()
    player_hand = [draw_card(card_deck), draw_card(card_deck)]
    dealer_hand = [draw_card(card_deck), draw_card(card_deck)]
    print(player_hand, "Hand Value: ", calculate_hand(player_hand))
    print(dealer_hand, "Hand Value: ", calculate_hand(dealer_hand))

if __name__ == '__main__' :
    main()

