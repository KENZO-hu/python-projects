import tkinter as tk
from tkinter import messagebox


class WelcomeScreen:
    def __init__(self, root, start_callback):
        self.root = root
        self.start_callback = start_callback
        self.frame = tk.Frame(root)
        self.frame.pack()

        tk.Label(self.frame, text="Welcome to Tic-Tac-Toe!", font=("Arial", 16)).pack(pady=10)

        tk.Label(self.frame, text="Player 1 (X) Name:").pack()
        self.player1_entry = tk.Entry(self.frame)
        self.player1_entry.pack(pady=5)

        tk.Label(self.frame, text="Player 2 (O) Name:").pack()
        self.player2_entry = tk.Entry(self.frame)
        self.player2_entry.pack(pady=5)

        tk.Button(self.frame, text="Start Game", command=self.start_game).pack(pady=10)

    def start_game(self):
        player1 = self.player1_entry.get().strip()
        player2 = self.player2_entry.get().strip()

        if not player1 or not player2:
            messagebox.showerror("Input Error", "Please enter names for both players.")
            return

        self.frame.destroy()
        self.start_callback(player1, player2)


class TicTacToeGame:
    def __init__(self, root, player1, player2):
        self.root = root
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1  # Player 1 starts
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.buttons = []

        self.frame = tk.Frame(root)
        self.frame.pack()

        self.status_label = tk.Label(self.frame, text=f"{self.current_player}'s Turn (X)", font=("Arial", 14))
        self.status_label.grid(row=0, column=0, columnspan=3, pady=10)

        self.create_board()
        self.create_restart_button()

    def create_board(self):
        for row in range(3):
            button_row = []
            for col in range(3):
                button = tk.Button(
                    self.frame, text="", font=("Arial", 20), width=5, height=2,
                    command=lambda r=row, c=col: self.make_move(r, c)
                )
                button.grid(row=row + 1, column=col, padx=5, pady=5)
                button_row.append(button)
            self.buttons.append(button_row)

    def create_restart_button(self):
        restart_button = tk.Button(self.frame, text="Restart Game", command=self.restart_game)
        restart_button.grid(row=4, column=0, columnspan=3, pady=10)

    def make_move(self, row, col):
        if self.board[row][col] != "":
            return

        mark = "X" if self.current_player == self.player1 else "O"
        self.board[row][col] = mark
        self.buttons[row][col].config(text=mark, state="disabled")

        if self.check_winner(row, col):
            self.status_label.config(text=f"{self.current_player} Wins!")
            self.disable_board()
        elif self.is_draw():
            self.status_label.config(text="It's a Draw!")
        else:
            self.switch_player()

    def switch_player(self):
        self.current_player = self.player1 if self.current_player == self.player2 else self.player2
        mark = "X" if self.current_player == self.player1 else "O"
        self.status_label.config(text=f"{self.current_player}'s Turn ({mark})")

    def check_winner(self, row, col):
        mark = self.board[row][col]

        # Check row
        if all(self.board[row][c] == mark for c in range(3)):
            return True

        # Check column
        if all(self.board[r][col] == mark for r in range(3)):
            return True

        # Check diagonals
        if row == col and all(self.board[i][i] == mark for i in range(3)):
            return True
        if row + col == 2 and all(self.board[i][2 - i] == mark for i in range(3)):
            return True

        return False

    def is_draw(self):
        return all(self.board[row][col] != "" for row in range(3) for col in range(3))

    def disable_board(self):
        for row in self.buttons:
            for button in row:
                button.config(state="disabled")

    def restart_game(self):
        self.frame.destroy()
        WelcomeScreen(self.root, lambda p1, p2: TicTacToeGame(self.root, p1, p2))


def main():
    root = tk.Tk()
    root.title("Tic-Tac-Toe")
    WelcomeScreen(root, lambda p1, p2: TicTacToeGame(root, p1, p2))
    root.mainloop()


if __name__ == "__main__":
    main()
