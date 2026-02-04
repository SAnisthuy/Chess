from tkinter import *


class Chess:
    def __init__(self):
        self.grid = []
        self.select = None
        self.prev = None
        self.turn = True
        self.track = set()

    def update_button(self, row, col, **kwargs):
        widgets = self.main.grid_slaves(row=row, column=col) 
        if widgets:
            btn = widgets[0]
            btn.config(**kwargs)

    def on_click(self, y, x):
        col = "gray" if (y + x) % 2 else "white"
        if self.select != None: # Selects an empty square with something previously selected
            print(self.track)
            if (y, x) in self.track:
                self.grid[y][x] = self.select
                self.select = None
                self.interact(y, x, reverse=True)
                self.update_button(y, x, image=self.pieces[self.grid[y][x]])
                self.update_button(self.prev[0], self.prev[1], image=self.pieces[0], bg=self.prev[2])
                self.prev =None
            else:
                print("Invalid move")

        elif self.select == None and self.grid[y][x] != 0: # Selects a non-empty square with nothing previously selected
            if self.turn and self.grid[y][x] < 10 or self.turn != True and self.grid[y][x] > 10:
                self.select = self.grid[y][x]
                self.update_button(y, x, bg="light green")
                self.prev = (y, x, col)
                self.interact(y, x)
                if self.turn:
                    self.turn = False
                else:
                    self.turn = True
                for i in self.grid:
                    print(i)
            else:
                pass
        else: # Neither
            print("Invalid interaction")
    
    def set_up(self):
        
        self.wPAWN = 1
        self.wBISHOP = 2
        self.wKNIGHT = 3
        self.wROOK = 4
        self.wQUEEN = 5
        self.wKING = 6

        self.bPAWN = 11
        self.bBISHOP = 12
        self.bKNIGHT = 13
        self.bROOK = 14
        self.bQUEEN = 15
        self.bKING = 16
        

        # Load pieces
        self.main.darkRook   = PhotoImage(file=r"DarkRook.png").subsample(6, 6)
        self.main.darkKnight = PhotoImage(file=r"DarkKnight.png").subsample(6, 6)
        self.main.darkBishop = PhotoImage(file=r"DarkBishop.png").subsample(6, 6)
        self.main.darkQueen  = PhotoImage(file=r"DarkQueen.png")
        self.main.darkKing   = PhotoImage(file=r"DarkKing.png").subsample(6, 6)
        self.main.darkPawn   = PhotoImage(file=r"DarkPawn.png").subsample(6, 6)

        self.main.whiteRook   = PhotoImage(file=r"LightRook.png").subsample(6, 6)
        self.main.whiteBishop = PhotoImage(file=r"LightBishop.png").subsample(4, 4)
        self.main.whiteKnight = PhotoImage(file=r"LightKnight.png").subsample(6, 6)
        self.main.whiteQueen  = PhotoImage(file=r"LightQueen.png").subsample(4, 4)
        self.main.whiteKing   = PhotoImage(file=r"LightKing.png").subsample(6, 6)
        self.main.whitePawn   = PhotoImage(file=r"LightPawn.png").subsample(6, 6)

        self.main.blank = PhotoImage(file=r"Blank.png")
        self.main.selected = PhotoImage(file=r"selected.png").subsample(6, 6)


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

    def interact(self, y, x, reverse=False):
        if reverse == False:
            if self.grid[y][x] == self.wPAWN:
                if self.grid[y-1][x] == 0: # If the square ahead is empty
                    self.update_button(y-1, x, image=self.main.selected) 
                    self.track.add((y-1, x))
                try:
                    if self.grid[y-1][x+1] != 0 or self.grid[y-1][x-1] != 0: # If square is empty and side square are not empty
                        if self.grid[y-1][x+1] == 0: # if this square is empty then pass
                            pass
                        else:
                            self.track.add((y-1, x+1))  # else add it to track

                        if self.grid[y-1][x-1] == 0: # If this square is empty then pass
                            pass
                        else:
                            self.track.add((y-1, x-1)) # else add it to track
                except IndexError:
                    if x == 7:
                        if self.grid[y+1][x-1] == 0: # If this square is empty then pass
                            pass
                        else:
                            self.track.add((y+1, x-1)) # else add it to track
                    elif x == 0:
                        if self.grid[y+1][x+1] == 0: # if this square is empty then pass
                            pass
                        else:
                            self.track.add((y+1, x+1))  # else add it to track


            if self.grid[y][x] == self.bPAWN: # Black pawn
                if self.grid[y+1][x] == 0: # check if square ahead is empty
                    self.update_button(y+1, x, image=self.main.selected)
                    self.track.add((y+1, x))
                try:
                    if self.grid[y+1][x+1] != 0 or self.grid[y+1][x-1] != 0: # If square is empty and side square are not empty
                        if self.grid[y+1][x+1] == 0: # if this square is empty then pass
                            pass
                        else:
                            self.track.add((y+1, x+1))  # else add it to track

                        if self.grid[y+1][x-1] == 0: # If this square is empty then pass
                            pass
                        else:
                            self.track.add((y+1, x-1)) # else add it to track
                except IndexError:
                    if x == 7:
                        if self.grid[y+1][x-1] == 0: # If this square is empty then pass
                            pass
                        else:
                            self.track.add((y+1, x-1)) # else add it to track
                    elif x == 0:
                        if self.grid[y+1][x+1] == 0: # if this square is empty then pass
                            pass
                        else:
                            self.track.add((y+1, x+1))  # else add it to track

            if self.grid[y][x] == self.wROOK: # White rook
                #horizontal up
                for i in range(y-1, 8):
                    if self.grid[i][x] != 0:
                        self.track.add((i, x))
                        break
                    else:
                        self.track.add((i, x))
                        self.update_button(i, x, image=self.main.select)
        else:
            for y, x in self.track:
                if self.grid[y][x] == 0:
                    self.update_button(y, x, image=self.main.blank)
            self.track = set()

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