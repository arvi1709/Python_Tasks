import tkinter as tk
from tkinter import messagebox

# Simple Tic Tac Toe for Two Players
class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        
        # 3x3 grid for buttons
        self.buttons = [[None, None, None], [None, None, None], [None, None, None]]
        
        # Track the current player (X or O)
        self.current_player = 'X'
        
        # Create buttons and set up the grid
        self.create_buttons()

    def create_buttons(self):
        for row in range(3):
            for col in range(3):
                # Create button with no text initially
                button = tk.Button(self.root, text='', font='Arial 20', height=3, width=6, 
                                   command=lambda r=row, c=col: self.handle_click(r, c))
                button.grid(row=row, column=col)
                self.buttons[row][col] = button

    # Handle when a button is clicked
    def handle_click(self, row, col):
        # Only mark if the button hasn't been clicked yet
        if self.buttons[row][col]['text'] == '':
            self.buttons[row][col]['text'] = self.current_player
            if self.check_winner(self.current_player):
                messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")
                self.reset_game()
            elif self.check_tie():
                messagebox.showinfo("Tic Tac Toe", "It's a tie!")
                self.reset_game()
            else:
                # Switch player
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    # Check if the current player has won
    def check_winner(self, player):
        for row in range(3):
            if all(self.buttons[row][col]['text'] == player for col in range(3)):
                return True
        for col in range(3):
            if all(self.buttons[row][col]['text'] == player for row in range(3)):
                return True
        if all(self.buttons[i][i]['text'] == player for i in range(3)) or all(self.buttons[i][2-i]['text'] == player for i in range(3)):
            return True
        return False

    # Check if the game is tied
    def check_tie(self):
        return all(self.buttons[row][col]['text'] != '' for row in range(3) for col in range(3))

    # Reset the game after win or tie
    def reset_game(self):
        for row in range(3):
            for col in range(3):
                self.buttons[row][col]['text'] = ''
        self.current_player = 'X'


# Main part of the program
if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
