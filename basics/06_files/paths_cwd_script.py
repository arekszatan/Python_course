import os

print("Absolute path to script file ", __file__)
script_dir = os.path.dirname(__file__)
print("Absolute path to script directory ", script_dir)

fh = open("new_file.txt", "w")
fh.write("Hello World!")
fh.close()

fh1 = open(script_dir + "\\new_file1.txt", "w")
fh1.write("Hello World!")
fh1.close()