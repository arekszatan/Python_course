import tkinter as tk

window = tk.Tk()

label1 = tk.Label(
    window,
    text="Label1",
    bg="red"
)
label1.pack(
    side="top",
    expand=True,
    fill="both"
)

label2 = tk.Label(
    window,
    text="Label1",
    bg="silver"
)
label2.pack(
    side="bottom",
    expand=True,
    fill="both"
)

button1 = tk.Button(
    window,
    bg="red",
    text="Button 1"
)
button1.pack(
    side="left",
    expand=True,
    fill="both"
)

button2 = tk.Button(
    window,
    bg="yellow",
    text="Button 1"
)
button2.pack(
    side="right",
    expand=True,
    fill="y"
)

window.mainloop()