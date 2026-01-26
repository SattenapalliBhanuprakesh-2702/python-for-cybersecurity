import socket
from concurrent.futures import ThreadPoolExecutor

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
        for p in exe.map(lambda x: scan_port(ip, x), range(1, 1025)):
            if p:
                open_ports.append(p)
    return open_ports

def banner_grab(ip, port):
    try:
        s = socket.socket()
        s.settimeout(2)
        s.connect((ip, port))
        data = s.recv(1024)
        s.close()
        return data.decode(errors="ignore")
    except:
        return ""

def risk_score(ports):
    risky = {21, 23, 3389}
    return sum(5 if p in risky else 1 for p in ports)
