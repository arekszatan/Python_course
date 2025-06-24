
fh = open("test.txt", "w")
fh.write("Content1\n")
fh.write("Content2\n")
fh.close()

fh2 = open("test.txt", "a")
fh2.write("Content3\n")
fh2.close()