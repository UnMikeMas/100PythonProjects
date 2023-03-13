import tkinter as tk

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.draw_board()
    
    def draw_board(self):
        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.master, text=self.board[i][j], font=("Arial", 20), width=5, height=2,
                                   command=lambda x=i, y=j: self.button_click(x, y))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)

    def button_click(self, x, y):
        if self.board[x][y] == " ":
            self.board[x][y] = self.current_player
            self.buttons[x][y].configure(text=self.current_player)
            if self.check_win():
                tk.messagebox.showinfo("Game Over", f"{self.current_player} wins!")
                self.reset_board()
            elif self.check_draw():
                tk.messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_board()
            else:
                self.switch_player()
    
    def check_win(self):
        # Check rows
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != " ":
                return True
        # Check columns
        for j in range(3):
            if self.board[0][j] == self.board[1][j] == self.board[2][j] != " ":
                return True
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return True
        return False

    def check_draw(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == " ":
                    return False
        return True

    def reset_board(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].configure(text=self.board[i][j])

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"
    
root = tk.Tk()
game = TicTacToe(root)
root.mainloop()