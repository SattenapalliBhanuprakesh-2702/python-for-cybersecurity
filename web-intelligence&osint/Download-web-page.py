import requests

url="https://google.com"
r=requests.get(url,timeout=10)
with open("page.html","w",encoding="utf-8") as f:
    f.write(r.text)