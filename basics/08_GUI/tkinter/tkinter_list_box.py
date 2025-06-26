import tkinter as tk

window = tk.Tk()

scrollbar = tk.Scrollbar(window)
list_box = tk.Listbox(window, selectmode="multiple")

scrollbar.pack(side="right", fill="y")
list_box.pack(fill="y")

scrollbar.config(command=list_box.yview)
list_box.config(yscrollcommand=scrollbar.set)

for i in range(15):
    list_box.insert(tk.END, str(i))

label = tk.Label(window)
label.pack()

def check_list():
    selection = list_box.curselection()
    label.config(text=str(selection))
    label.after(300, check_list)

check_list()

window.mainloop()