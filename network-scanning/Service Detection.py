import socket

def detect_service(ip,port):
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
    target="127.0.0.1"
    ports=[80,22,21]
    for p in ports:
        banner=detect_service(target,p)
        if banner:
            print(p,"->",banner.splitlines()[0])
