import tkinter as tk

window = tk.Tk()

scrollbar = tk.Scrollbar(window)
text_box = tk.Text(window, height=5, width=30, padx=5, pady=5, font="Times 18 bold")
scrollbar.pack(side="right", fill="y")
text_box.pack(side="left", fill="y")
scrollbar.config(command=text_box.yview)
text_box.config(yscrollcommand=scrollbar.set)

text_box.insert("end", "Hello World!\nHello again!")

print("Text data: ", text_box.get(1.0, "end"))


window.mainloop()