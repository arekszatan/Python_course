import os, sys
import urllib.parse
import validators # pip install validators
import requests
from datetime import datetime

print("Number of arguments: ", len(sys.argv))
print("Arguments list: ", sys.argv)

url = "https://duckduckgo.com"
if len(sys.argv) > 1:
    url = sys.argv[1]

print("Website to download: ", url)

script_dir = os.path.dirname(__file__)
os.chdir(script_dir)
print("Current working dir: ", os.getcwd())

if not os.path.exists("./websites"):
    os.mkdir("./websites")

parser_url = urllib.parse.urlparse(url)
print(parser_url)

valid_flag = validators.url(url)
if valid_flag:
    print("Url: ", url, "is valid")
else:
    print("Url: ", url, "is invalid")
    raise Exception("Bad url")

response = requests.get(url, allow_redirects=True)
if response.ok:
    print("Response ok from server for url: ", url)
    now = datetime.now()
    date_string = now.strftime("%d.%m.%Y %H:%M:%S")
    print(date_string)
    file_name = "./websites/" + parser_url.netloc + " " + date_string + ".html"
    print(file_name)
    fh = open(file_name, "wb")
    fh.write(response.content)
    fh.close()
