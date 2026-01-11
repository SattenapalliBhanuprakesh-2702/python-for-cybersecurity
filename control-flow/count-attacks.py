logs=[
    {"ip":"192.168.1.10","status":"failed"},
    {"ip":"10.10.10.10","status":"success"},
    {"ip":"192.168.1.10","status":"failed"},
    {"ip":"192.168.1.10","status":"failed"},
    {"ip":"192.168.1.10","status":"failed"}
]

attack_count={}
for log in logs:
    if log["status"]=="failed":
        ip=log["ip"]
        attack_count[ip]=attack_count.get(ip,0)+1
print(attack_count)