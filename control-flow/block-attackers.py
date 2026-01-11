attack_count={"192.168.1.10":7,"10.0.0.5":4}

for ip,count in attack_count.items():
    if count >5:
        print("block account",ip)
    else:
        print("Allow",ip)