def find_attackers(counts,thresold=5):
    attackers=[]
    for ip,count in counts.items():
        if count>thresold:
            attackers.append(ip)
    return attackers

counts={"192.168.1.10":7,"10.0.0.5":4}
print(find_attackers(counts))