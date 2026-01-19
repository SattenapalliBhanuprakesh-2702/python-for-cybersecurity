import re
import requests

html=requests.get("https://Email.com").text

emails=re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",html)
print(set(emails))