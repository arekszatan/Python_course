import os
import shutil

script_dir = os.path.dirname(__file__)

fh = open(script_dir + "/test.txt", "w", encoding="utf-8")
fh.write("Dane ńąćźż")
fh.close()

if not os.path.exists(script_dir + "/new_test.txt"):
    os.rename(script_dir + "/test.txt",
              script_dir + "/new_test.txt")

print(os.path.getsize(script_dir + "/new_test.txt"))

print(os.path.isfile(script_dir + "/new_test.txt"))
print(os.path.isdir(script_dir + "/new_test.txt"))
print(os.path.isdir("./basic"))

if not os.path.exists(script_dir + "/sub_dir"):
    os.rmdir(script_dir + "/sub_dir")

if not os.path.exists(script_dir + "/sub_dir"):
    os.mkdir(script_dir + "/sub_dir")

if os.path.exists(script_dir + "/new_test.txt"):
    os.remove(script_dir + "/new_test.txt")

print("Current working dir: ", os.getcwd())
cwd1 = os.getcwd()
os.chdir("..")
cwd2 = os.getcwd()
if cwd1 == cwd2:
    print("The same patch")
else:
    print("Different cwd")
print("Current working dir: ", os.getcwd())

if not os.path.exists(script_dir + "/data_copy.dat"):
    shutil.copyfile(script_dir + "/data.dat", script_dir + "/data_copy.dat")