import os

print("Current working directory: ", os.getcwd())

files = os.listdir()
print(files) # current working dir

files1 = os.listdir("..")
print(files1)

files2 = os.listdir("../programs")
print(files2)

files3 = os.listdir("../01_data_types")
print(files3)

files4 = os.listdir("../../challenges")
print(files4)