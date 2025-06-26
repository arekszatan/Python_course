import tkinter as tk

window = tk.Tk()

def value_changed():
    if cb_value.get() == 0:
        print("Check box is off")
    elif cb_value.get() == 1:
        print("Check box is on")

cb_value = tk.IntVar(value=0)
c1 = tk.Checkbutton(window, text="Accept TOS", variable=cb_value,
                    onvalue=1, offvalue=0, command=value_changed)
c1.grid(row=0)

window.mainloop()