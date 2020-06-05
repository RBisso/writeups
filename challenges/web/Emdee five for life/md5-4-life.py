import re
import requests
import hashlib

url = 'http://docker.hackthebox.eu:31841/'
req = requests.session()

h = req.get(url)
h = re.search("<h3 align='center'>.*?</h3>", h.text)
h = re.search(">.*?<",h.group())
h = str(h.group())
h = h.replace('<','').replace('>','')
print(h)
hashed = hashlib.md5(h.encode()).hexdigest()
print(hashed)
data = {'hash':hashed}
res = req.post(url,data)
print(res.text)
