from tkinter import *

main = Tk()

buttons = [[None for _ in range(8)] for _ in range(8)]
main.blank = PhotoImage(file=r"Blank.png")

for i in range(8):
    for j in range(8):
        color = "gray" if (i + j) % 2 else "white"
        btn = Button(main, bg=color)  # no width/height here
        btn.grid(row=i, column=j, sticky="nsew")
        buttons[i][j] = btn
        buttons[i][j].config(image=main.blank)

for i in range(8):
    main.grid_rowconfigure(i, weight=1)
    main.grid_columnconfigure(i, weight=1)

# Load and downscale ALL pieces to the same size
main.darkRook   = PhotoImage(file=r"DarkRook.png").subsample(6, 6)
main.darkKnight = PhotoImage(file=r"DarkKnight.png").subsample(6, 6)
main.darkBishop = PhotoImage(file=r"DarkBishop.png").subsample(6, 6)
main.darkQueen  = PhotoImage(file=r"DarkQueen.png")
main.darkKing   = PhotoImage(file=r"DarkKing.png").subsample(6, 6)
main.darkPawn   = PhotoImage(file=r"DarkPawn.png").subsample(6, 6)

main.whiteRook = PhotoImage(file=r"LightRook.png").subsample(6, 6)
main.whiteBishop = PhotoImage(file=r"LightBishop.png").subsample(6, 6)
main.whiteKnight = PhotoImage(file=r"LightKnight.png").subsample(6, 6)
main.whiteQueen = PhotoImage(file=r"LightQueen.png").subsample(4, 4)
main.whiteKing = PhotoImage(file=r"LightKing.png").subsample(6, 6)
main.whitePawn = PhotoImage(file=r"LightPawn.png").subsample(6, 6)


# Place pieces
buttons[0][0].config(image=main.darkRook)
buttons[0][1].config(image=main.darkKnight)
buttons[0][2].config(image=main.darkBishop)
buttons[0][3].config(image=main.darkQueen)
buttons[0][4].config(image=main.darkKing)
buttons[0][5].config(image=main.darkBishop)
buttons[0][6].config(image=main.darkKnight)
buttons[0][7].config(image=main.darkRook)

for i in range(8):
    buttons[1][i].config(image=main.darkPawn)

buttons[7][0].config(image=main.whiteRook)
buttons[7][1].config(image=main.whiteKnight)
buttons[7][2].config(image=main.whiteBishop)
buttons[7][3].config(image=main.whiteQueen)
buttons[7][4].config(image=main.whiteKing)
buttons[7][5].config(image=main.whiteBishop)
buttons[7][6].config(image=main.whiteKnight)
buttons[7][7].config(image=main.whiteRook)

for i in range(8):
    buttons[6][i].config(image=main.whitePawn)

main.mainloop()
