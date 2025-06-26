import tkinter as tk
import yfinance as yf

window = tk.Tk()
window.title("Stock Info")

top_widget = tk.Frame(window)

label = tk.Label(top_widget, text="Write stock ticker:")
label.pack(side="left")
entry = tk.Entry(top_widget)
entry.pack(side="right")
top_widget.pack()

scrollbar = tk.Scrollbar(window)
text_box = tk.Text(window, height=15, width=90, padx=5, pady=5, font="Helvetica 12")
scrollbar.pack(side="right", fill="y")
text_box.pack(expand=True, fill= "both")
scrollbar.config(command=text_box.yview)
text_box.config(yscrollcommand=scrollbar.set)

def download_data(e):
    text_box.delete("1.0", tk.END)
    stock = str(e.widget.get())

    if not stock:
        print("No stock ticker")
        return

    stock = stock.upper().strip()
    print("Download stock data: ", stock)
    stock_data = yf.Ticker(stock)
    print(stock_data.info)
    text_box.insert(tk.END,"Ticker: " + stock + " \n\n")

    for key in stock_data.info.keys():
        try:
            v = str(key) + ": " + stock_data.info[str(key)] + " \n\n"
            text_box.insert(tk.END, v)
        except:
            pass

    # 1mo, 1m, 1d, 1y, 1wk
    history = stock_data.history(period="1mo", interval="1d")
    text_box.insert(tk.END, history)

entry.bind("<Return>", download_data)


window.mainloop()