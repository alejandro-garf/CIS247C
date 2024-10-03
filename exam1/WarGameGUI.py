# WarGameGUI.py

import tkinter as tk
from tkinter import messagebox
from WarCardGame import initialize_game, draw_card, compare_cards, collect_cards, shuffle_deck, break_tie


class WarGameGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("War Card Game")

        self.main_frame = tk.Frame(self.master, padx=20, pady=20)
        self.main_frame.pack(expand=True, fill=tk.BOTH)

        self.player_deck, self.computer_deck = initialize_game()
        self.winner = None

        self.player_card_var = tk.StringVar()
        self.computer_card_var = tk.StringVar()
        self.player_deck_count_var = tk.StringVar(value=f"Deck Count: {len(self.player_deck)}")
        self.player_deck_var = tk.StringVar(value=" ".join(self.player_deck))

        self.create_widgets()

    def create_widgets(self):
        self.computer_card_label = tk.Label(self.main_frame, textvariable=self.computer_card_var, font=("Helvetica", 16))
        self.computer_card_label.pack(pady=(10, 20))

        self.player_card_label = tk.Label(self.main_frame, textvariable=self.player_card_var, font=("Helvetica", 16))
        self.player_card_label.pack(pady=(10, 10))

        self.player1_deck_count_label = tk.Label(self.main_frame, textvariable=self.player_deck_count_var, font=("Helvetica", 12))
        self.player1_deck_count_label.pack()

        self.player1_deck_label = tk.Label(self.main_frame, textvariable=self.player_deck_var, font=("Helvetica", 10), wraplength=500)
        self.player1_deck_label.pack()

        self.buttons_frame = tk.Frame(self.main_frame)
        self.buttons_frame.pack(pady=(10, 0))

        self.play_card_button = tk.Button(self.buttons_frame, text="Play Card", command=self.play_card)
        self.play_card_button.pack(side=tk.LEFT, padx=5)

        self.battle_button = tk.Button(self.buttons_frame, text="Battle!!!", command=self.battle_cards)
        self.battle_button.pack(side=tk.LEFT, padx=5)

        self.winner_gather_button = tk.Button(self.buttons_frame, text="Winner take cards", command=self.winner_gather_cards)
        self.winner_gather_button.pack(side=tk.LEFT, padx=5)

        self.shuffle_cards_button = tk.Button(self.buttons_frame, text="Shuffle Hand", command=self.shuffle_cards)
        self.shuffle_cards_button.pack(side=tk.LEFT, padx=5)

    def play_card(self):
        if not self.player_card_var.get() == '':
            messagebox.showinfo("Error", "Winner must take cards.")
            return

        if self.player_deck and self.computer_deck:
            player_card = draw_card(self.player_deck)
            computer_card = draw_card(self.computer_deck)
            self.player_card_var.set(f"Player Card: {player_card}")
            self.computer_card_var.set(f"Computer Card: {computer_card}")
            self.player_deck_count_var.set(f"Deck Count: {len(self.player_deck)}")
            self.player_deck_var.set(" ".join(self.player_deck))
        else:
            messagebox.showinfo("Game Over", "The game has ended.")

    def battle_cards(self):
        if self.player_card_var.get() == '':
            messagebox.showinfo("Error", "Must first play card.")
            return

        player_card = self.player_card_var.get().split("Card: ")[1]
        computer_card = self.computer_card_var.get().split("Card: ")[1]
        self.winner = compare_cards(player_card, computer_card)
        if self.winner == 'Tie':
            message = 'Tie'
        else:
            message = f'{self.winner} wins!'
            if self.winner == 'Player':
                self.player_card_label.config(fg="red")
            elif self.winner == 'Computer':
                self.computer_card_label.config(fg="red")
        messagebox.showinfo("Hand Result", message)

    def winner_gather_cards(self):
        if not self.winner:
            messagebox.showinfo("Error", "Must first battle!!!")
            return

        player_card = self.player_card_var.get().split("Card: ")[1]
        computer_card = self.computer_card_var.get().split("Card: ")[1]
        if self.winner == 'Player':
            collect_cards(self.player_deck, [player_card, computer_card])
        elif self.winner == 'Computer':
            collect_cards(self.computer_deck, [player_card, computer_card])
        elif self.winner == 'Tie':
            tie_broken = break_tie(self.player_deck, self.computer_deck, [player_card, computer_card])
            if not tie_broken:
                collect_cards(self.player_deck, [player_card])
                collect_cards(self.computer_deck, [computer_card])
        else:
            messagebox.showinfo("Error", "Winner must be 'Player' or 'Computer'")
            return

        self.player_card_label.config(fg="black")
        self.computer_card_label.config(fg="black")
        self.player_deck_count_var.set(f"Deck Count: {len(self.player_deck)}")
        self.player_deck_var.set(" ".join(self.player_deck))

        if not self.player_deck or not self.computer_deck:
            winner_text = "Player wins!" if self.player_deck else "Computer wins!"
            messagebox.showinfo("Game Over", winner_text)
            self.play_button.config(state="disabled")

        self.winner = None
        self.player_card_var.set("")
        self.computer_card_var.set("")

    def shuffle_cards(self):
        shuffle_deck(self.player_deck)
        self.player_deck_var.set(" ".join(self.player_deck))

    def placeholder_action(self):
        messagebox.showinfo("Placeholder", "This button doesn't do anything yet.")


def main():
    root = tk.Tk()
    app = WarGameGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
