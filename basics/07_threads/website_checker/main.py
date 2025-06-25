from website import *
import os, sys
import threading, time
import requests
import validators

script_dir = os.path.dirname(__file__)
os.chdir(script_dir)
# print(websites.get_next_website_to_check())
# websites.put_website_data({"index" : 0, "website" : "duckduckgo.com", "status_code" : 200})
# websites.save_report()

data_lock = threading.Lock()

class Client(threading.Thread):
    def __init__(self, thread_name, websites, sleep_time):
        threading.Thread.__init__(self)
        self.thread_name = thread_name
        self.websites = websites
        self.sleep_time = sleep_time

    def run(self):
        while True:
            data_lock.acquire()
            website_to_check = self.websites.get_next_website_to_check()
            data_lock.release()
            if not website_to_check:
                break
            print(website_to_check)
            self.check_url(website_to_check)
            time.sleep(self.sleep_time)
        print(self.thread_name, " ended!")

    def check_url(self, data):
        try:
            valid_url_flag = validators.url(data["website"])
            if valid_url_flag:
                data["valid_url_flag"] = True
                response = requests.get(data["website"], allow_redirects=True)
                data["status_code"] = response.status_code
            else:
                data["valid_url_flag"] = False
        except:
            data["exception"] = sys.exc_info()[0]

        data_lock.acquire()
        self.websites.put_website_data(data)
        data_lock.release()

websites = Websites("website.txt")
# client1 = Client("client1", websites, 0.1)
# client1.start()
# client1.join()
num_threads = 10
threads_list = []
num = 0
while num < num_threads:
    t = Client("T" + str(num), websites, 0.1)
    threads_list.append(t)
    num += 1
    t.start()

for t in threads_list:
    t.join()

websites.save_report()
print("Job done!")