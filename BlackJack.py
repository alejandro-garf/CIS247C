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

def calculate_hand_value(hand):

    value = sum(card_value(card) for card in hand) #generator expression
    ace_count = hand.count('A')

    if value > 21 and ace_count > 0:
        value -= 10
        ace_count -= 1

    return value


def main():
    card_deck = initialize_deck()
    player_hand = [draw_card(card_deck), draw_card(card_deck)]
    dealer_hand = [draw_card(card_deck), draw_card(card_deck)]

    while True:
        player_value = calculate_hand_value(player_hand)
        print(f"Your face up card: {player_hand}  Value: {player_value}")
        print(f"Dealer face up card: {dealer_hand[0]} ")

        if player_value > 21:
            print("You bust! Game Over!")
            break

        action = input("Do you want to (H)it or (S)tand? (Type H for hit or S for stand): ").upper()

        if action == 'H':
            player_hand.append(draw_card(card_deck))
        elif action == 'S':
            print(f"Dealer shows his face down card: {dealer_hand[1]}" )
            dealer_value = calculate_hand_value(dealer_hand)
            while dealer_value < 17:
                new_card = draw_card(card_deck)
                print(f"Dealer picks new card: {new_card}")
                dealer_hand.append(new_card)
                dealer_value = calculate_hand_value(dealer_hand)

            print (f"Dealers Hand: {dealer_hand}   Value: {dealer_value}")
            if dealer_value > 21:
                print("Dealer Busts! You Win!")
            elif dealer_value > player_value:
                print("Dealer Wins!")
            elif player_value > dealer_value:
                print("Player Wins!")
            else:
                print("It's a tie!")
            break


        else:
            print("Invalid Input")





if __name__ == '__main__' :
    main()


