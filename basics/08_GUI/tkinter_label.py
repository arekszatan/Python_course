import tkinter as tk
import os

script_dir = os.path.dirname(__file__)
os.chdir(script_dir)

window = tk.Tk()
window.title("Application")
logo = tk.PhotoImage(file="img.png")

label1 = tk.Label(
    window,
    text="Hello World!",
    foreground="red",
    background="green",
    width=20,
    height=3,
    cursor="heart",
    font="Times 18 bold italic underline",
    anchor="center",
    padx=10,
    pady=10
)
label1.pack()

label2 = tk.Label(window, text="Hello World again!")
label2.pack()

label3 = tk.Label(
    window,
    text="Hello World!",
    image=logo,
    width=200,
    height=200,
    foreground="red",
    compound="center"
)
label3.pack()

label3.config(text="Hello World!\n Hello Again!")

window.mainloop()