# WarCardGame.py
import random


def initialize_game():
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
        return player_deck.pop(0)  # Changed: Now removes the first card instead of a random card
    return None


def compare_cards(player_card, computer_card):
    card_values = {str(i): i for i in range(2, 11)}  # Added: Dictionary to map card values
    card_values.update({'J': 11, 'Q': 12, 'K': 13, 'A': 14})  # Added: Face card values

    if card_values[player_card] > card_values[computer_card]:
        return 'Player'
    elif card_values[player_card] < card_values[computer_card]:
        return 'Computer'
    else:
        return 'Tie'


def collect_cards(winner_deck, player_card,
                  computer_card):  # Changed: Added player_card and computer_card as parameters
    winner_deck.append(player_card)  # Changed: Appends player_card to winner_deck
    winner_deck.append(computer_card)  # Changed: Appends computer_card to winner_deck
    return winner_deck


def break_tie(player_deck, computer_deck, tie_cards):  # Added: New function to handle tie-breaks
    if len(player_deck) < 4 or len(computer_deck) < 4:
        # If either player doesn't have enough cards, game over
        return 'Game Over', tie_cards

    # Draw 3 face-down cards from each deck
    player_down = [draw_card(player_deck) for _ in range(3)]
    computer_down = [draw_card(computer_deck) for _ in range(3)]

    # Draw the 4th card face-up
    player_up = draw_card(player_deck)
    computer_up = draw_card(computer_deck)

    tie_cards.extend(player_down + computer_down + [player_up, computer_up])

    result = compare_cards(player_up, computer_up)

    if result == 'Player':
        return 'Player', tie_cards
    elif result == 'Computer':
        return 'Computer', tie_cards
    else:
        # Another tie, recursively call break_tie
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
    import subprocess
    import sys

    subprocess.run([sys.executable, 'WarGameGUI.py'])
    sys.exit()