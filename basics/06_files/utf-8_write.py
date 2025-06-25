import os

script_dir = os.path.dirname(__file__)
print("Script directory: ", script_dir)

fh = open(script_dir + "/ogonki.txt", "w", encoding="utf-8")
fh.write("tekst z ogonkami: ąęćńś\n")
fh.write("tekst z ogonkami: ąęćńś\n")
fh.write("tekst z ogonkami: ąęćńś\n")
fh.close()