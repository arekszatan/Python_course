import tkinter as tk
from tkinter import messagebox
import requests
from threading import Thread
import time
from datetime import datetime

class WebsiteCheckerApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.url_entry = None
        self.add_button = None
        self.websites_list = None

        self.title("Website Checker")
        self.geometry("800x600")
        self.websites = [
            {"url" : "https://onet.pl", "last_checked" : None},
            {"url": "https://google.com", "last_checked": None},
            {"url": "https://ithardware.pl", "last_checked": None}
        ]
        self.create_widgets()
        self.update_website_list()
        Thread(target=self.start_checking, daemon=True).start()

    def create_widgets(self):
        self.url_entry = tk.Entry(self)
        self.url_entry.pack(pady=20)

        self.add_button = tk.Button(self, text="Add Website", command=self.add_website)
        self.add_button.pack(pady=20)

        self.websites_list = tk.Listbox(self, width=100, height=15)
        self.websites_list.pack(fill="both", expand=True, padx=20, pady=20)

    def add_website(self):
        url = self.url_entry.get()
        if url:
            self.websites.append({"url" : url, "last_checked" : None})
            self.update_website_list()
            self.url_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "URL cannot be empty.")

    def update_website_list(self):
        self.websites_list.delete(0, tk.END)
        for website in self.websites:
            last_checked = website["last_checked"] if website["last_checked"] else "Not checked yet"
            display_text = f"{website['url']} - Last checked: {last_checked}"
            self.websites_list.insert(tk.END, display_text)

    def check_website(self, website):
        try:
            response = requests.get(website["url"], timeout=5)
            status = "OK" if response.status_code == 200 else "Bad request"
        except requests.exceptions.RequestException as e:
            status = "Bad requests"
        return status

    def start_checking(self):
        while True:
            for i, website in enumerate(self.websites):
                status = self.check_website(website)
                last_checked = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
                self.update_website_status(i, website['url'], status, last_checked)
            time.sleep(5)

    def update_website_status(self, index, url, status, last_checked):
        def update():
            display_text = f"{url} - {status} - Last checked: {last_checked}"
            self.websites_list.delete(index)
            self.websites_list.insert(index, display_text)
            self.websites[index]['last_checked'] = last_checked
        self.after(100, update)

if __name__ == "__main__":
    app = WebsiteCheckerApp()
    app.mainloop()