import threading, time

data = ["Adam", "Ola", "Kasia", "Daniel", "Rafał"]
data_lock = threading.Lock()

class SomeThread(threading.Thread):
    def __init__(self, thread_name, data_len, sleep_time):
        threading.Thread.__init__(self)
        self.thread_name = thread_name
        self.data_len = data_len
        self.sleep_time = sleep_time

    def run(self):
        num = 0
        while num < self.data_len:
            data_lock.acquire()
            data[num] = data[num] + " " + str(num)
            print(self.thread_name, data[num])
            data_lock.release()
            time.sleep(self.sleep_time)
            num += 1
        print(self.thread_name, " ended!")


t1 = SomeThread("Thread-1", len(data), 0.001)
t2 = SomeThread("Thread-2", len(data), 0.001)
t3 = SomeThread("Thread-3", len(data), 0.001)

t1.start()
t2.start()
t3.start()
print("-- Thread-2 status: ", t2.is_alive())

t1.join()
t2.join()
t3.join()
print("-- Thread-2 status: ", t2.is_alive())
print("All thread ended")