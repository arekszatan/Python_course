import tkinter as tk

window = tk.Tk()

label1 = tk.Label(window, text="label 1", bg="silver")
label1.place(x=0, y=10, width=50, height=25)

label2 = tk.Label(window, text="label 2", bg="red")
label2.place(x=70, y=70, width=90, height=25)


window.mainloop()