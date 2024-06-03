import tkinter as tk
from tkinter import ttk
import random

def nobutt(button):

    button.bind("<Enter>", func=lambda e: button.place(x=random.randrange(0,350), y= random.randrange(0,200)))


def yes():
    print('<3')

root = tk.Tk()
root.geometry('400x250')
root.resizable(True, True)
root.title('butao')

prompt = tk.Label(
    root,
    text = "Quer namorar cmg?",
    anchor=tk.CENTER,
    justify=tk.CENTER)

prompt.config(font =("Inter", 14))

prompt.pack(pady=50)

yesbutton = tk.Button(
    root, 
    text='SIM', 
    command=yes,
    )


yesbutton.pack()
yesbutton.place(x=50, y=150)
yesbutton.config(width=10, height=1, font=("Inter",14))

nobutton = tk.Button(
root, 
text='NÃO'
)

nobutton.pack()
nobutton.place(x=210, y=150)
nobutton.config(width=10, height=1, font=("Inter",14))
nobutt(nobutton)

root.mainloop()

