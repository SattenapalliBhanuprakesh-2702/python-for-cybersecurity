import re

text = "Visit http://evil.com and https://secure.org"

urls=re.findall(r"https?://[a-zA-Z0-9./_-]+",text)
print(urls)