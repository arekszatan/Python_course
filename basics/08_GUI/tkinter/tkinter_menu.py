import tkinter as tk

window = tk.Tk()

def menu_item_selected():
    print("Menu item selected")

def menu_item_close_selected():
    quit()

root_menu = tk.Menu()
file_menu = tk.Menu()
file_menu.add_command(label="New", command=menu_item_selected)
file_menu.add_command(label="Open", command=menu_item_selected)
file_menu.add_command(label="Save", command=menu_item_selected)
file_menu.add_command(label="Save as", command=menu_item_selected)
file_menu.add_separator()
file_menu.add_command(label="Close", command=menu_item_close_selected)

root_menu.add_cascade(label="File", menu=file_menu)

window.config(menu=root_menu)

window.mainloop()