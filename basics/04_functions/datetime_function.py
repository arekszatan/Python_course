import time
import datetime

ticks = time.time()
print(ticks)

time_data = time.localtime()
print(time_data)
print(time_data.tm_year)
print(time_data.tm_mon)
print(time_data.tm_hour)
print(time_data.tm_min)

time_data = time.localtime(10)
print(time_data)

result = time.asctime(time.localtime())
print(result)

time_data = time.localtime()
print(time.strftime("%d/%m/%Y %H:%M:%S", time_data))

time_str = "17:23:45 08.12.2021"
time_data = time.strptime(time_str, "%H:%M:%S %d.%m.%Y")
print(time_data)

i = 0
while i < 10:
    time.sleep(0.05)
    print(time.asctime(time.localtime()))
    i += 1

time_start = time.perf_counter()
time.sleep(0.1)
time_end = time.perf_counter()
print("Code took: ", time_end - time_start)

data_time_obj = datetime.datetime.now()
print(data_time_obj)
# print(dir(data_time_obj))

date_time_obj = datetime.datetime(2025, 3, 10, 22, 59, 59)
print("date(): ", date_time_obj.date())
print("time(): ", date_time_obj.time())
print("timestamp(): ", date_time_obj.timestamp())
print("today(): ", date_time_obj.today())
print("year: ", date_time_obj.year)
print("month: ", date_time_obj.month)
print("day: ", date_time_obj.day)
print("hour: ", date_time_obj.hour)
print("minute: ", date_time_obj.minute)
print("second: ", date_time_obj.second)

print("format: ", date_time_obj.strftime("%H:%M:%S %d/%m/%Y"))

date_time_obj = date_time_obj.now()
print("format: ", date_time_obj.strftime("%H:%M:%S %d/%m/%Y"))

date_time_1 = datetime.datetime(2025, 1, 1, 23, 59, 59)
date_time_2 = datetime.datetime(2030, 1, 1, 23, 59, 59)

print(date_time_2 > date_time_1)
print(date_time_2 < date_time_1)
print(date_time_2 == date_time_1)
print(date_time_2 != date_time_1)

date1 = datetime.date(2025, 1, 1)
date2 = datetime.date(2030, 1, 1)

print(date2 > date1)
print(date2 < date1)
print(date2 == date1)
print(date2 != date1)


