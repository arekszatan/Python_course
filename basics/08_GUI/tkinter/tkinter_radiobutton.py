import tkinter as tk

window = tk.Tk()

def radio_clicked():
    print("Radio value: ", radio_value.get())

radio_value = tk.IntVar()

radio1 = tk.Radiobutton(window, text="option 1", variable=radio_value,
                        value=1, command=radio_clicked)
radio2 = tk.Radiobutton(window, text="option 2", variable=radio_value,
                        value=2, command=radio_clicked)
radio3 = tk.Radiobutton(window, text="option 3", variable=radio_value,
                        value=3, command=radio_clicked)

radio1.pack()
radio2.pack()
radio3.pack()

window.mainloop()