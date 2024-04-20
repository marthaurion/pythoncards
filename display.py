import card
import os
from tkinter import Tk, Label, PhotoImage

temp = card.Card(1,1)

root = Tk()

img = PhotoImage(file=os.path.join("card_image",str(temp)+".png"))
my_image = Label(root, image=img)
my_image.pack()

root.mainloop()
