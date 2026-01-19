import re
import requests
from bs4 import BeautifulSoup

url="https://google.com"
data=requests.get(url).text

emails=re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",data)

ips=re.findall(r"\b(?:\d{1,3}\.){3}\d{1,3}\b",data)

soup=BeautifulSoup(data,"html.parser")
links=[link.get("href") for link in soup.find_all("a") if link.get("href")]

print(emails)
print(ips)
print(links)