# WarCardGame.py

#Alejandro Fonseca Exam Number One

import subprocess
import sys
import random


def initialize_game():
    """
    - Initialize a standard 52-card deck.
    - Shuffle the deck.
    - Divide the deck equally between two players.
    """

    deck = [str(i) for i in range(2, 11)] + ['J', 'Q', 'K', 'A']
    deck = deck * 4  # Ignore suit

    shuffle_deck(deck)

    player1_deck = deck[:len(deck) // 2]
    player2_deck = deck[len(deck) // 2:]

    return player1_deck, player2_deck


def shuffle_deck(deck):
    random.shuffle(deck)
    return deck


def draw_card(player_deck):
    if player_deck:
        return player_deck.pop(0)
    return None

def compare_cards(player_card, computer_card):
    card_values = {str(i): i for i in range(2, 11)}
    card_values.update({'J': 11, 'Q': 12, 'K': 13, 'A': 14})

    if card_values[player_card] > card_values[computer_card]:
        return 'Player'
    elif card_values[player_card] < card_values[computer_card]:
        return 'Computer'
    else:
        return 'Tie'

## This part caused me immense pain, I eventually gave up due to time but holy
def collect_cards(player_deck, computer_deck, player_card=None, computer_card=None, winner=None):
    if not player_card or not computer_card or not winner:
        print("collect_cards: Missing arguments, cannot proceed.")
        return player_deck, computer_deck, len(player_deck)

    if winner == 'Player':
        player_deck.append(player_card)
        player_deck.append(computer_card)
    elif winner == 'Computer':
        computer_deck.append(player_card)
        computer_deck.append(computer_card)

    return player_deck, computer_deck, len(player_deck)

def break_tie(player_deck, computer_deck, tie_cards):
    if len(player_deck) < 4 or len(computer_deck) < 4:
        return 'Game Over', player_deck, computer_deck

    player_down = [draw_card(player_deck) for _ in range(3)]
    computer_down = [draw_card(computer_deck) for _ in range(3)]

    player_up = draw_card(player_deck)
    computer_up = draw_card(computer_deck)

    tie_cards.extend(player_down + computer_down + [player_up, computer_up])

    result = compare_cards(player_up, computer_up)

    if result == 'Player':
        player_deck.extend(tie_cards)
        return 'Player', player_deck, computer_deck
    elif result == 'Computer':
        computer_deck.extend(tie_cards)
        return 'Computer', player_deck, computer_deck
    else:
        return break_tie(player_deck, computer_deck, tie_cards)


def check_game_over(player_deck, computer_deck):
    return not player_deck or not computer_deck


def get_winner(player_deck, computer_deck):
    if len(player_deck) > len(computer_deck):
        return "Player wins!"
    elif len(player_deck) < len(computer_deck):
        return "Computer wins!"
    else:
        return "It's a tie!"


if __name__ == "__main__":
    """
    Entry point for the program.
    It will call the WarGameGUI.py to start the GUI.
    """

    subprocess.run([sys.executable, 'WarGameGUI.py'])
    sys.exit()
