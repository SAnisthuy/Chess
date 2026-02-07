from tkinter import *


class Chess:
    def __init__(self):
        self.grid = []
        self.select = None
        self.prev = None
        self.turn = True
        self.track = set()
        self.check_track = False
        self.checking = False

    def update_button(self, row, col, **kwargs):
        widgets = self.main.grid_slaves(row=row, column=col) 
        if widgets:
            btn = widgets[0]
            btn.config(**kwargs)

    def test_movement(self, y, x, p):
        c = self.checking
        if p < 10:
            if self.grid[y][x] == 0 or self.grid[y][x] > 10:
                if c and self.grid[y][x] == 16:
                    self.check_track = True
                    self.update_button(y, x, bg='red')
                self.track.add((y, x))
                if not c:
                    self.update_button(y, x, bg='orange')
        else:
            if self.grid[y][x] == 0 or self.grid[y][x] < 10:
                if c and self.grid[y][x] == 6:
                    self.check_track = True
                    self.update_button(y, x, bg='red')

                self.track.add((y, x))
                if not c:
                    self.update_button(y, x, bg='orange')

    def cancel_move(self, y, x):
        self.update_button(self.prev[0], self.prev[1], bg=self.prev[2])
        self.select = None
        self.interact(y, x, reverse=True)
        self.prev =None
        if self.turn:
            self.turn = False
        else:
            self.turn = True
            
    def promotion(self, y, x, p):
        self.promote = Toplevel(self.main)
        self.promote.geometry('125x275+1250+276')

        b, k, r, q = 2, 3, 4, 5
        if p > 10:
            b, k, r, q = 12, 13, 14, 15
            self.promote.geometry('125x275+1250+560')
        
        self.promote.title("Promotion")
        self.promote.overrideredirect(True)

        Queen = Button(self.promote, image=self.pieces[q], command=lambda: self.promotion2(y, x, q))
        Rook = Button(self.promote,image=self.pieces[r], command=lambda: self.promotion2(y, x, r))
        Knight = Button(self.promote,image=self.pieces[k], command=lambda: self.promotion2(y, x, k))
        Bishop = Button(self.promote,image=self.pieces[b], command=lambda: self.promotion2(y, x, b))

        Queen.pack()
        Rook.pack()
        Bishop.pack()
        Knight.pack()

    def promotion2(self, y, x, val):
        self.grid[y][x] = val 
        self.update_button(y, x, image=self.pieces[val])
        self.promote.destroy()

    def end(self):
        self.main.quit()
        self.main.destroy()
        win = Tk()
        self.center_window(250, 250, win)
        win.config(bg='green')
        win_text = Label(win, text="GAME OVER", font=("Helvetica", 16, "bold"))
        win_text.pack(anchor=CENTER)
        mainloop()


    def center_window(self, width, height, root):
        # Get screen width and height
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Calculate x and y coordinates for the center of the screen
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        # Set the geometry
        root.geometry(f'{width}x{height}+{x}+{y}')

    def on_click(self, y, x):
        col = "gray" if (y + x) % 2 else "white"

        if self.select != None: # Selects an empty square with something previously selected
            if (y, x) in self.track:
                if (self.select == self.wPAWN and y == 0) or (self.select == self.bPAWN and y == 7):
                    self.promotion(y, x, self.select)
                elif self.grid[y][x] == self.wKING or self.grid[y][x] == self.bKING:
                    self.end()
                    return None
                else:
                    # update new square
                    self.grid[y][x] = self.select 
                    self.update_button(y, x, image=self.pieces[self.grid[y][x]]) 
                # update previous square
                self.update_button(self.prev[0], self.prev[1], image=self.pieces[0], bg=self.prev[2]) 
                self.grid[self.prev[0]][self.prev[1]] = 0
                # clear move highlights
                self.interact(y, x, reverse=True)
                # clear variables
                self.prev, self.select = None, None
                self.checking = True
                self.interact(y, x)
                self.checking = False

            else:
                self.cancel_move(y, x)


        elif self.select == None and self.grid[y][x] != 0: # Selects a non-empty square with nothing previously selected
            if self.turn and self.grid[y][x] < 10 or self.turn != True and self.grid[y][x] > 10:
                self.select = self.grid[y][x]
                self.update_button(y, x, bg="light green")
                self.prev = (y, x, col)
                self.interact(y, x)
                self.check_track = False
                if self.turn:
                    self.turn = False
                else:
                    self.turn = True
            else:
                pass
        else: # Neither
            pass
    
    def pawn(self, p, y, x):
            if p == self.wPAWN:
                if self.grid[y-1][x] == 0:
                    if y == 6 and self.grid[y-2][x] == 0:
                        self.test_movement(y-2, x, p)
                    self.test_movement(y-1, x, p)
                if x > 0 and self.grid[y-1][x-1] > 10:
                    self.test_movement(y-1, x-1, p)
                
                if x < 7 and self.grid[y-1][x+1] > 10:
                    self.test_movement(y-1, x+1, p)
                
            else:
                if self.grid[y+1][x] == 0:
                    if y == 1 and self.grid[y+2][x] == 0:
                        self.test_movement(y+2, x, p)
                    self.test_movement(y+1, x, p)
                if x > 0 and 0 < self.grid[y+1][x-1] < 10:
                    self.test_movement(y+1, x-1, p)
                
                if x < 7 and 0 < self.grid[y+1][x+1] < 10:
                    self.test_movement(y+1, x+1, p)

    def knight(self, p, y, x):
        # up
        if y >= 2:
            if x != 0:
                self.test_movement(y-2, x-1, p)
            if x != 7:
                self.test_movement(y-2, x+1, p)
        # down
        if y <= 5:
            if x != 0:
                self.test_movement(y+2, x-1, p)
            if x != 7:
                self.test_movement(y+2, x+1, p)
        # right
        if x <= 5:
            if y != 0:
                self.test_movement(y-1, x+2, p)
            if y != 7:
                self.test_movement(y+1, x+2, p)
        
        # left
        if x >= 2:
            if y != 0:
                self.test_movement(y-1, x-2, p)
            if y != 7:
                self.test_movement(y+1, x-2, p)

    def bishop(self, p, y, x):
        # down and right
        if abs(x-8) > abs(y-8):
            l = abs(y-8)
        else:
            l = abs(x-8)
        for i in range(1, l):
            curr = self.grid[y+i][x+i]
            self.test_movement(y+i, x+i, p)
            if curr != 0:
                break
    
        # down and left
        if abs(x-(-1)) > abs(y-8):
            l = abs(8-y)
        else:
            l = abs(x-(-1))
        for i in range(1, l):
            curr = self.grid[y+i][x-i]
            self.test_movement(y+i, x-i, p)
            if curr != 0:
                break

        # up and right
        if abs(x-8) > abs(y-(-1)):
            l = abs((-1)-y)
        else:
            l = abs(x-8)
        for i in range(1, l):
            curr = self.grid[y-i][x+i]
            self.test_movement(y-i, x+i, p)
            if curr != 0:
                break

        # up and left
        if abs(x-(-1)) > abs(y-(-1)):
            l = abs((-1)-y)
        else:
            l = abs(x-(-1))
        for i in range(1, l):
            curr = self.grid[y-i][x-i]
            self.test_movement(y-i, x-i, p)
            if curr != 0:
                break
            
    def rook(self, p, y, x):
        # vertical up
        for i in range(y-1, -1, -1):
            curr = self.grid[i][x]
            self.test_movement(i, x, p)
            if curr != 0:
                break

        # vertical down
        for i in range(y+1, 8):
            curr = self.grid[i][x]
            self.test_movement(i, x, p)
            if curr != 0:
                break

        # horizontal right
        for i in range(x+1, 8):
            curr = self.grid[y][i]
            self.test_movement(y, i, p)
            if curr != 0:
                break
        
        # horizontal left
        for i in range(x-1, -1, -1):
            curr = self.grid[y][i]
            self.test_movement(y, i, p)
            if curr != 0:
                break

    def king(self, p, y, x):
            #up 
            if y != 0:
                self.test_movement(y-1, x, p)
            # down
            if y != 7:
                self.test_movement(y+1, x, p)
            #left 
            if x != 0:
                self.test_movement(y, x-1, p)
            if x != 7:
                self.test_movement(y, x+1, p)
            # up and right
            if y != 0 and x != 7:
                self.test_movement(y-1, x+1, p)
            # up and left
            if y != 0 and x != 0:
                self.test_movement(y-1, x-1, p)
            # down and right
            if y!= 7 and x != 7:
                self.test_movement(y+1, x+1, p)
            # down and left
            if y != 7 and x != 0:
                self.test_movement(y+1, x-1, p)

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
        self.main.darkQueen  = PhotoImage(file=r"DarkQueen.png").subsample(6, 6)
        self.main.darkKing   = PhotoImage(file=r"DarkKing.png").subsample(6, 6)
        self.main.darkPawn   = PhotoImage(file=r"DarkPawn.png").subsample(6, 6)

        self.main.whiteRook   = PhotoImage(file=r"LightRook.png").subsample(6, 6)
        self.main.whiteBishop = PhotoImage(file=r"LightBishop.png").subsample(6, 6)
        self.main.whiteKnight = PhotoImage(file=r"LightKnight.png").subsample(6, 6)
        self.main.whiteQueen  = PhotoImage(file=r"LightQueen.png").subsample(6, 6)
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
                self.pawn(1, y, x)

            elif self.grid[y][x] == self.bPAWN: # Black pawn
                self.pawn(11, y, x)
    
            elif self.grid[y][x] == self.wROOK: # White rook
                self.rook(self.wROOK, y, x)

            elif self.grid[y][x] == self.bROOK: # Black rook
                self.rook(self.bROOK, y, x)

            elif self.grid[y][x] == self.wBISHOP: # Black bishop
                self.bishop(self.wBISHOP, y, x)

            elif self.grid[y][x] == self.bBISHOP: # Black rook
                self.bishop(self.bBISHOP, y, x)

            elif self.grid[y][x] == self.wQUEEN:
                self.bishop(self.wBISHOP, y, x)
                self.rook(self.wROOK, y, x)

            elif self.grid[y][x] == self.bQUEEN:
                self.bishop(self.bBISHOP, y, x)
                self.rook(self.bROOK, y, x)

            elif self.grid[y][x] == self.wKING:
                self.king(self.wKING, y, x)
            
            elif self.grid[y][x] == self.bKING:
                self.king(self.bKING, y, x)

            elif self.grid[y][x] == self.wKNIGHT:
                self.knight(self.wKNIGHT, y, x)

            elif self.grid[y][x] == self.bKNIGHT:
                self.knight(self.bKNIGHT, y, x)

        else:
            for y, x in self.track:
                color = "gray" if (y + x) % 2 else "white"
                self.update_button(y, x, bg=color)
            self.track = set()

    def run(self):
    
        self.main = Tk()

        self.main.title("Chess")
        self.center_window(528, 528, self.main)

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