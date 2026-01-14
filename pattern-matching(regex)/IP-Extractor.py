import re

log = "192.168.1.10 failed\n10.0.0.5 success\n8.8.8.8 failed"
ips=re.findall(r"\b(?:\d{1,3}\.){3}\d{1,3}\b",log)
print(ips)