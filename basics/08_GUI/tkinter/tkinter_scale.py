import tkinter as tk

window = tk.Tk()

value = tk.DoubleVar()
scale = tk.Scale(window, from_=0, to=60,
                 orient="vertical", variable=value)
scale.pack(anchor="center")

def selected():
    selection = "Value: " + str(value.get())
    label.config(text=selection)
    label.after(200, selected)

label = tk.Label(window)
label.pack()
selected()

window.mainloop()