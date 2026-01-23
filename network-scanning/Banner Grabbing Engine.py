import socket

def grab_banner(ip,port):
    
    try:
        s=socket.socket()
        s.settimeout(2)
        s.connect((ip,port))
        s.send(b"HEAD / HTTP/1.0\r\n\r\n")
        banner=s.recv(1024).decode(errors="ignore")
        s.close()
        return banner.strip()
    
    except Exception:
        return None
    
    
if __name__=="__main__":
    target=[("127.0.0.1",80),("127.0.0.1",22)]
    
    for ip,port in target:
        banner=grab_banner(ip,port)
        
        if banner:
            print(ip,port,banner)