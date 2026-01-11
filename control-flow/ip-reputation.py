ip="192.168.1.10"
blacklist=["10.0.0.1","192.168.1.10"]
if ip in blacklist:
    print("Block the ip",ip)
else:
    print(ip,"is clean")