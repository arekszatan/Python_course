import threading, time

class SomeThread(threading.Thread):
    def __init__(self, thread_name, sleep_time):
        threading.Thread.__init__(self)
        self.thread_name = thread_name
        self.sleep_time = sleep_time

    def run(self):
        num = 0
        max = 6
        while num < max:
            local_time = time.localtime()
            print(self.thread_name, time.strftime("%H:%M:%S", local_time))
            time.sleep(self.sleep_time)
            num += 1
        print(self.thread_name, " ended!")


t1 = SomeThread("Thread-1", 0.1)
t2 = SomeThread("Thread-2", 0.3)
t3 = SomeThread("Thread-3", 0.4)

t1.start()
t2.start()
t3.start()

time.sleep(1)
print("-- Thread-2 status: ", t2.is_alive())

t1.join()
t2.join()
t3.join()
print("-- Thread-2 status: ", t2.is_alive())
print("All thread ended")