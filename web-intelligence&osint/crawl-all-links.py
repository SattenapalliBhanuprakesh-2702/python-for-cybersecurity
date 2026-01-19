import requests
from bs4 import BeautifulSoup

url="https://google.com"
soup=BeautifulSoup(requests.get(url).text,"html.parser")
for link in soup.find_all("a"):
    href=link.get("href")
    if href:
        print(href)
