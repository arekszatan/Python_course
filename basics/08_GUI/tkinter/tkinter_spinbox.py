import tkinter as tk

window = tk.Tk()

def spin_value():
    label.config(text=str(spin.get()))

spin = tk.Spinbox(window, from_=0, to=50, command=spin_value)
spin.pack()

label = tk.Label(window)
label.pack()

window.mainloop()