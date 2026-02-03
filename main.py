from tkinter import *

clicked = []
# random change
def on_click(y, x):
    global clicked, buttons, main

    current_img_name = buttons[y][x].cget("image")

    if current_img_name == str(main.blank):
        if clicked:
            buttons[y][x].config(image=clicked[0])
            clicked.pop(0)
    else:
        clicked.append(buttons[y][x].image_obj)
        buttons[y][x].config(image=main.blank)
        buttons[y][x].image_obj = main.blank

main = Tk()

buttons = [[None for _ in range(8)] for _ in range(8)]
main.blank = PhotoImage(file=r"Blank.png")

for i in range(8):
    for j in range(8):
        color = "gray" if (i + j) % 2 else "white"
        btn = Button(main, bg=color,
                     command=lambda r=i, c=j: on_click(r, c))
        btn.grid(row=i, column=j, sticky="nsew")
        btn.config(image=main.blank)
        btn.image_obj = main.blank  
        buttons[i][j] = btn

for i in range(8):
    main.grid_rowconfigure(i, weight=1)
    main.grid_columnconfigure(i, weight=1)

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

#helper function
def set_piece(r, c, img):
    buttons[r][c].config(image=img)
    buttons[r][c].image_obj = img

# Place pieces
set_piece(0, 0, main.darkRook)
set_piece(0, 1, main.darkKnight)
set_piece(0, 2, main.darkBishop)
set_piece(0, 3, main.darkQueen)
set_piece(0, 4, main.darkKing)
set_piece(0, 5, main.darkBishop)
set_piece(0, 6, main.darkKnight)
set_piece(0, 7, main.darkRook)

for i in range(8):
    set_piece(1, i, main.darkPawn)

set_piece(7, 0, main.whiteRook)
set_piece(7, 1, main.whiteKnight)
set_piece(7, 2, main.whiteBishop)
set_piece(7, 3, main.whiteQueen)
set_piece(7, 4, main.whiteKing)
set_piece(7, 5, main.whiteBishop)
set_piece(7, 6, main.whiteKnight)
set_piece(7, 7, main.whiteRook)

for i in range(8):
    set_piece(6, i, main.whitePawn)

main.mainloop()
