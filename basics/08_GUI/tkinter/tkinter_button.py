import tkinter as tk

window = tk.Tk()

def button_clicked():
    print("Clicked!")

button = tk.Button(
    window,
    text="QUIT",
    border=10,
    foreground="red",
    background="green",
    activeforeground="black",
    activebackground="blue",
    font="Times 10 bold",
    height=1,
    width=1,
    padx=10,
    pady=10,
    relief="groove",
    command=button_clicked
)

button.pack()
window.mainloop()