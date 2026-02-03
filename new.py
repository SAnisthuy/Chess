from tkinter import *


class Chess:
    def __init__(self):
        self.grid = []
        self.select = None
        self.prev = None

    def update_button(self, row, col, **kwargs):
        widgets = self.main.grid_slaves(row=row, column=col) 
        if widgets:
            btn = widgets[0]
            btn.config(**kwargs)

    def on_click(self, y, x):
        col = "gray" if (y + x) % 2 else "white"
        if self.select != None: # Selects an empty square with something previously selected

            self.grid[y][x] = self.select
            self.select = None
            self.update_button(y, x, image=self.pieces[self.grid[y][x]])
            self.update_button(self.prev[0], self.prev[1], image=self.pieces[0], bg=self.prev[2])
            self.prev =None

        elif self.select == None and self.grid[y][x] != 0: # Selects a non-empty square with nothing previously selected

            self.select = self.grid[y][x]
            self.update_button(y, x, bg="light green")
            self.prev = (y, x, col)

        else: # Neither
            print("Invalid interaction")
    
    def set_up(self):
        # Load pieces
        self.main.darkRook   = PhotoImage(file=r"DarkRook.png").subsample(6, 6)
        self.main.darkKnight = PhotoImage(file=r"DarkKnight.png").subsample(6, 6)
        self.main.darkBishop = PhotoImage(file=r"DarkBishop.png").subsample(6, 6)
        self.main.darkQueen  = PhotoImage(file=r"DarkQueen.png")
        self.main.darkKing   = PhotoImage(file=r"DarkKing.png").subsample(6, 6)
        self.main.darkPawn   = PhotoImage(file=r"DarkPawn.png").subsample(6, 6)

        self.main.whiteRook   = PhotoImage(file=r"LightRook.png").subsample(6, 6)
        self.main.whiteBishop = PhotoImage(file=r"LightBishop.png").subsample(6, 6)
        self.main.whiteKnight = PhotoImage(file=r"LightKnight.png").subsample(6, 6)
        self.main.whiteQueen  = PhotoImage(file=r"LightQueen.png").subsample(4, 4)
        self.main.whiteKing   = PhotoImage(file=r"LightKing.png").subsample(6, 6)
        self.main.whitePawn   = PhotoImage(file=r"LightPawn.png").subsample(6, 6)

        self.main.blank = PhotoImage(file=r"Blank.png")

        # map
        self.pieces = {0: self.main.blank, 
                1: self.main.whitePawn, 
                2: self.main.whiteBishop, 
                3: self.main.whiteKnight, 
                4: self.main.whiteRook, 
                5: self.main.whiteQueen,
                6: self.main.whiteKing, 
                11: self.main.darkPawn,
                12: self.main.darkBishop,
                13: self.main.darkKnight,
                14: self.main.darkRook,
                15: self.main.darkQueen,
                16: self.main.darkKing}

        for i in range(8):
            row = []
            for i in range(8):
                row.append(0)
            self.grid.append(row)

        # rooks
        self.grid[0][0], self.grid[0][7] = 14, 14
        self.grid[7][0], self.grid[7][7] = 4, 4

        # knights
        self.grid[0][1], self.grid[0][6] = 13, 13
        self.grid[7][1], self.grid[7][6] = 3, 3

        # bishops
        self.grid[0][2], self.grid[0][5] = 12, 12
        self.grid[7][2], self.grid[7][5] = 2, 2

        # king and queens
        self.grid[0][4], self.grid[7][4] = 16, 6
        self.grid[0][3], self.grid[7][3] = 15, 5

        # pawns
        for i in range(8):
            self.grid[1][i] = 11
            self.grid[6][i] = 1

    def run(self):
    
        self.main = Tk()

        self.set_up()
        for i in range(8):
            for j in range(8):
                color = "gray" if (i + j) % 2 else "white"
                btn = Button(self.main, image= self.pieces[self.grid[i][j]], command=lambda r=i, c=j: self.on_click(r, c))
                btn.config(bg=color)
                btn.grid(row=i, column=j, sticky="nsew")

        mainloop()


run = Chess()
run.run()