import re

data="""
    user=admin pass=123456
    login=root password=hacked
"""

cred=re.findall(r"(user|login)=([a-zA-Z0-9_]+).*?(pass|password)=([a-zA-Z0-9]+)",data)

for c in cred:
    print("Username:",c[1],"password:",c[3])