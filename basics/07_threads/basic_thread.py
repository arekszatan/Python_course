import _thread
import time

def print_time(thread_name, sleep_time):
    num = 0
    max = 6
    while num < max:
        local_time = time.localtime()
        print(thread_name, time.strftime("%H:%M:%S", local_time))
        time.sleep(sleep_time)
        num += 1
    print(thread_name, " ended!")

_thread.start_new_thread(print_time, ("Thread 1", 0.5))
_thread.start_new_thread(print_time, ("Thread 2", 0.3))

print("Print after thread!")
while True:
    pass