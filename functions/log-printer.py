def log_printers(logs):
    for log in logs:
        print("ip :",log["ip"])
        print("user :",log["user"])
        print("status :",log["status"])
        print("-"*25)

logs=[{"ip":"192.168.1.10","user":"admin","status":"failed"},
    {"ip":"192.168.1.10","user":"admin","status":"failed"},
    {"ip":"10.10.10.10","user":"guest","status":"success"},
    {"ip":"172.168.1.10","user":"root","status":"failed"}
]

log_printers(logs)