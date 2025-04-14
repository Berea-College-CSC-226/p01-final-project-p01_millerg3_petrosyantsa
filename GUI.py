import tkinter as tk


class TkinterGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.minsize(width=100, height=100)
        self.root.maxsize(width=1000, height=500)
        self.rows = [1, 2, 3, 4, 5, 6, 7, 8]
        self.columns = [1, 2, 3, 4, 5, 6, 7, 8]
        self.square = None
        self.pepperoni = None
        self.sausage = None
        self.square_pos = []
        self.pepperoni_pos = []
        self.sausage_pos = []
        self.row = None
        self.col = None
        # self.piece = None
        # self.board = list(range(1, 65))
        # self.pieces = []

    def create_board(self):
        for self.row in self.rows:
            for self.col in self.columns:
                self.square_pos.append(self.row+self.col)
                self.square = tk.Button(self.root, width=15, height=3, command=self.button_handler(self.row + self.col))
                self.square.grid(row = self.row, column = self.col)


    def create_pieces(self):
        for self.row in self.rows[:3]: # Puts starting pieces in first 3 rows
            for self.col in self.columns:
                if (self.row + self.col) % 2 != 0: # Alternates spots for pieces
                    self.pepperoni = tk.Button(self.root, width=5, height=1)
                    self.pepperoni_pos.append(self.row + self.col)
                    # print(self.pepperoni_pos)
                    self.pepperoni.grid(row=self.row, column=self.col)

        for self.row in self.rows[5:]: # Puts starting pieces in bottom 3 rows
            for self.col in self.columns:
                if (self.row + self.col) % 2 != 0:
                    self.sausage = tk.Button(self.root, width=5, height=1)
                    self.sausage_pos.append(self.row + self.col)
                    # print(self.sausage_pos)
                    self.sausage.grid(row=self.row, column=self.col)

    def button_handler(self):
            print(self.square.grid)
                    # print(self.square_pos.index(self.square))
        # if self.square_pos == self.sausage_pos + 2 or self.square_pos == self.sausage_pos:
















def main():
    myGUI = TkinterGUI()
    myGUI.create_board()
    myGUI.create_pieces()

    myGUI.root.mainloop()

if __name__ == "__main__":
    main()