def check_failure(log):
    return log["status"]=="failed"

logs=[{"ip":"192.168.1.10","user":"admin","status":"failed"},
    {"ip":"192.168.1.10","user":"admin","status":"failed"},
    {"ip":"10.10.10.10","user":"guest","status":"success"},
    {"ip":"172.168.1.10","user":"root","status":"failed"}
]

for log in logs:
    validation=check_failure(log)
    if validation:
        print(log["user"],"is Suspicious")
    else:
        print(log["user"],"is valid")
    print("-"*20)
    