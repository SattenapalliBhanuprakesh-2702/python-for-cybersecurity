import socket
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

RISKY_PORTS = {21, 23, 25, 110, 139, 445, 3389}

def scan_port(ip, port):
    try:
        s = socket.socket()
        s.settimeout(1)
        s.connect((ip, port))
        s.close()
        return port
    except:
        return None

def scan_host(ip):
    open_ports = []
    with ThreadPoolExecutor(max_workers=100) as exe:
        results = exe.map(lambda p: scan_port(ip, p), range(1, 1025))
        for r in results:
            if r:
                open_ports.append(r)
    return open_ports

def banner(ip, port):
    try:
        s = socket.socket()
        s.settimeout(2)
        s.connect((ip, port))
        data = s.recv(1024)
        s.close()
        return data.decode(errors="ignore")
    except:
        return ""

def threat_score(ports):
    score = 0
    for p in ports:
        if p in RISKY_PORTS:
            score += 5
        else:
            score += 1
    return score

def log_siem(ip, score):
    with open("siem.log", "a") as f:
        f.write(f"{datetime.now()} | {ip} | THREAT_SCORE {score}\n")

def main():
    target = "127.0.0.1"
    ports = scan_host(target)
    score = threat_score(ports)
    log_siem(target, score)
    print("Ports:", ports)
    print("Threat score:", score)

main()
