import os, pickle

script_dir = os.path.dirname(__file__)

number = 12312
list_data = ["Ania", "Ola", "Kasia", 12312]
str_data = "Tekst z ogonkami: ąśćńż"

fh = open(script_dir + "/data.dat", "wb")
pickle.dump(number, fh)
pickle.dump(list_data, fh)
pickle.dump(str_data, fh)
fh.close()

fh = open(script_dir + "/data.dat", "rb")
number_info = pickle.load(fh)
list_data_info = pickle.load(fh)
str_data_info = pickle.load(fh)
fh.close()

print(number_info)
print(list_data_info)
print(str_data_info)