from tkinter import *

grid = []
select = None


for i in range(8):
    row = []
    for i in range(8):
        row.append(0)
    grid.append(row)

# rooks
grid[0][0], grid[0][7] = 14, 14
grid[7][0], grid[7][7] = 4, 4

# knights
grid[0][1], grid[0][6] = 13, 13
grid[7][1], grid[7][6] = 3, 3

# bishops
grid[0][2], grid[0][5] = 12, 12
grid[7][2], grid[7][5] = 2, 2

# king and queens
grid[0][4], grid[7][4] = 16, 6
grid[0][3], grid[7][3] = 15, 5

# pawns
for i in range(8):
    grid[1][i] = 11
    grid[6][i] = 1


def on_click(y, x):
    global select
    if grid[y][x] == 0 and select != None:
        grid[y][x] = select
        select = None
    elif select == None and grid[y][x] != 0:
        select = grid[y][x]
        
    else:
        print("Invalid interaction")
    
main = Tk()

# Load pieces
main.darkRook   = PhotoImage(file=r"DarkRook.png").subsample(6, 6)
main.darkKnight = PhotoImage(file=r"DarkKnight.png").subsample(6, 6)
main.darkBishop = PhotoImage(file=r"DarkBishop.png").subsample(6, 6)
main.darkQueen  = PhotoImage(file=r"DarkQueen.png")
main.darkKing   = PhotoImage(file=r"DarkKing.png").subsample(6, 6)
main.darkPawn   = PhotoImage(file=r"DarkPawn.png").subsample(6, 6)

main.whiteRook   = PhotoImage(file=r"LightRook.png").subsample(6, 6)
main.whiteBishop = PhotoImage(file=r"LightBishop.png").subsample(6, 6)
main.whiteKnight = PhotoImage(file=r"LightKnight.png").subsample(6, 6)
main.whiteQueen  = PhotoImage(file=r"LightQueen.png").subsample(4, 4)
main.whiteKing   = PhotoImage(file=r"LightKing.png").subsample(6, 6)
main.whitePawn   = PhotoImage(file=r"LightPawn.png").subsample(6, 6)

main.blank = PhotoImage(file=r"Blank.png")

# map
pieces = {0: main.blank, 
          1: main.whitePawn, 
          2: main.whiteBishop, 
          3: main.whiteKnight, 
          4: main.whiteRook, 
          5: main.whiteQueen,
          6: main.whiteKing, 
          11: main.darkPawn,
          12: main.darkBishop,
          13: main.darkKnight,
          14: main.darkRook,
          15: main.darkQueen,
          16: main.darkKing}


# Tkinter

for i in range(8):
    for j in range(8):
        color = "gray" if (i + j) % 2 else "white"
        btn = Button(main, bg=color, image= pieces[grid[i][j]], command=lambda r=i, c=j: on_click(r, c))
        btn.grid(row=i, column=j, sticky="nsew")

mainloop()