import socket
from concurrent.futures import ThreadPoolExecutor

def scan_port(ip,port,timeout=1):
    try:
        s=socket.socket()
        s.settimeout(timeout)
        s.connect((ip,port))
        s.close()
        return port
    except Exception:
        return None

def scan_host(ip,ports):
    try:
        open_ports=[]
        
        with ThreadPoolExecutor(max_workers=100) as executor:
            results=executor.map(lambda p: scan_port(ip,p), ports)
            
            for r in results:
                if r:
                    open_ports.append(r)
                    
        return open_ports 
    except Exception:
        return None
    

if __name__=="__main__":
    target="127.0.0.1"
    ports=range(1,120)
    results=scan_host(target,ports)
    print("open ports :",results)       