logs=[
    {"ip":"192.168.1.10","status":"failed"},
    {"ip":"10.10.10.10","status":"success"},
    {"ip":"192.168.1.10","status":"failed"},
    {"ip":"192.168.1.10","status":"failed"},
    {"ip":"192.168.1.10","status":"failed"}
]

def count_failures(logs):
    counts={}
    for log in logs:
        if log['status']=="failed":
            ip=log["ip"]
            counts[ip]=counts.get(ip,0)+1
    return counts

def find_attacker(counts,thresold=3):
    attackers=[]
    for ip,count in counts.items():
        if count>=thresold:
            attackers.append(ip)
    return attackers

def attackers(attackers):
    for ip in attackers:
        print("Alert :",ip,"triggered brute-force detection")
        print("Action : Recommend firewall blocks")
        print("-"*40)

# ----------main---------------------#
failure_count=count_failures(logs)
attackers_ip=find_attacker(failure_count)
attackers(attackers_ip)