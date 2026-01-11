ip=[
    {"ip":"192.168.1.10","user":"admin","status":"failed"},
    {"ip":"10.10.10.10","user":"guest","status":"success"},
    {"ip":"172.168.1.10","user":"root","status":"failed"}
]
print(ip[0]["ip"])
print(ip[2]["status"])