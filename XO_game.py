import tkinter as tk
import random

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")

        self.board = [" " for _ in range(9)]
        self.current_player = "X"

        self.buttons = []
        for i in range(3):
            for j in range(3):
                button = tk.Button(root, text=" ", font=("Helvetica", 16), width=5, height=2,
                                   command=lambda row=i, col=j: self.on_button_click(row, col))
                button.grid(row=i, column=j)
                self.buttons.append(button)

    def on_button_click(self, row, col):
        index = 3 * row + col
        if self.board[index] == " ":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player, state=tk.DISABLED)
            if self.check_winner():
                self.show_winner()
            elif " " not in self.board:
                self.show_tie()
            else:
                self.switch_player()
                self.computer_move()

    def computer_move(self):
        empty_cells = [i for i in range(9) if self.board[i] == " "]
        if empty_cells:
            computer_choice = random.choice(empty_cells)
            self.board[computer_choice] = "O"
            self.buttons[computer_choice].config(text="O", state=tk.DISABLED)
            if self.check_winner():
                self.show_winner()
            elif " " not in self.board:
                self.show_tie()
            else:
                self.switch_player()

    def switch_player(self):
        self.current_player = "X" if self.current_player == "O" else "O"

    def check_winner(self):
        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                                (0, 3, 6), (1, 4, 7), (2, 5, 8),
                                (0, 4, 8), (2, 4, 6)]

        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != " ":
                return True
        return False

    def show_winner(self):
        winner = self.current_player if self.current_player == "X" else "O"
        tk.messagebox.showinfo("Game Over", f"Player {winner} wins!")
        self.reset_game()

    def show_tie(self):
        tk.messagebox.showinfo("Game Over", "It's a tie!")
        self.reset_game()

    def reset_game(self):
        for i in range(9):
            self.board[i] = " "
            self.buttons[i].config(text=" ", state=tk.NORMAL)
        self.current_player = "X"


if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()

