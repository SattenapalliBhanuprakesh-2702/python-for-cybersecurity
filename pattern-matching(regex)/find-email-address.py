import re

data="admin@test.com  attacker@evil.net  user@gmail.com"

emails=re.findall(r"[a-zA-Z0-9.+%-_]+@[a-zA-Z0-9-.]+\.[a-zA-Z]{2,}",data)
print(emails)