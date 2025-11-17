from tkinter import *

main = Tk()


for i in range(8):
    for j in range(8):
        if i % 2 == 0 and j % 2 != 0:
            Button(main, width=10, height=5, bg="gray").grid(row=i, column=j)
        elif i % 2 == 1 and j % 2 == 0:
            Button(main, width=10, height=5, bg="gray").grid(row=i, column=j)
        else:
            Button(main, width=10, height=5, bg="white").grid(row=i, column=j)
def set_up():

    #Rooks
    main.lightrook = PhotoImage(file="LightRook.png")
    # image_path = "DarkRook.png"
    # darkrook = PhotoImage(file=image_path)
    # # knights
    # image_path = "DarkKnight.png"
    # darkknight = PhotoImage(file=image_path)
    # image_path = "LightKnight.png"
    # lightknight = PhotoImage(file=image_path)
    # #bishops
    # image_path = "DarkBishop.png"
    # darkbishop = PhotoImage(file=image_path)
    # image_path = "LightBishop.png"
    # lightbishop = PhotoImage(file=image_path)
    # #Queen
    # # image_path = "DarkQueen.png"
    # # darkqueen = PhotoImage(file=image_path)
    # # image_path = "LightQueen.png"
    # # lightqueen = PhotoImage(file=image_path)
    # #King
    # image_path = "DarkKing.png"
    # darkking = PhotoImage(file=image_path)
    # image_path = "LightKing.png"
    # lightking = PhotoImage(file=image_path)

    Button(main, image=photoimage, width=10, height=5).grid(row=0, column=5)

set_up()

mainloop()