import os

script_dir = os.path.dirname(__file__)

fh = open(script_dir + "/ogonki.txt", "r", encoding="utf-8")
lines = fh.readlines()
fh.close()
for line in lines:
    print(line)

fh = open(script_dir + "/ogonki.txt", "r", encoding="utf-8")
while True:
    line = fh.readline()
    if not line:
        break
    print(line)
fh.close()