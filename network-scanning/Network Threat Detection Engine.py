def detect_threats(scan_items):
    
    threats=[]
    risky_ports={21,23,3389}
    for ip,ports in scan_items.items():
        for p in ports:
            if p in risky_ports:
                threats.append((ip,p))
    
    return threats


if __name__=="__main__":
    scan_items={
        "192.168.1.10": [22, 21],
        "192.168.1.20": [80]
    }
    
    print(detect_threats(scan_items))