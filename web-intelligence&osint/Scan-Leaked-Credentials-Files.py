import re

data=open("leaks.txt").read()

emails=re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",data)
passwords=re.findall(r"pass=\w+",data)

print("Emails :",emails)
print("passwords :",passwords)