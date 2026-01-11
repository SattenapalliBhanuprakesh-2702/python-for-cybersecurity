def count_failure_ip(logs):
    count={}
    for log in logs:
        if log["status"]=="failed":
            ip=log["ip"]
            count[ip]=count.get(ip,0)+1
    return count

logs=[
    {"ip":"192.168.1.10","status":"failed"},
    {"ip":"10.10.10.10","status":"success"},
    {"ip":"192.168.1.10","status":"failed"},
    {"ip":"192.168.1.10","status":"failed"},
    {"ip":"192.168.1.10","status":"failed"}
]

print(count_failure_ip(logs))