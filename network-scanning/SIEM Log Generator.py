from datetime import datetime

def write_siem_event(ip,port,severity):
    event=f"{datetime.now()} | Alerts | ip {ip} | port {port} | severity {severity}"
    
    with open("siem.log","a") as f:
        f.write(event)
        
write_siem_event("192.168.1.10", 21, "HIGH")