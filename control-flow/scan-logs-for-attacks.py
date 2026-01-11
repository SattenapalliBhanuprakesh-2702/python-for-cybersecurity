ip=[
    {"ip":"192.168.1.10","user":"admin","status":"failed"},
    {"ip":"10.10.10.10","user":"guest","status":"success"},
    {"ip":"172.168.1.10","user":"root","status":"failed"}
]
for i in range(3):
    if ip[i]["status"]=="failed":
        print(ip[i]["user"],"login is failed and their ip is",ip[i]["ip"])
    else:
        print(ip[i]["user"],"valid user")