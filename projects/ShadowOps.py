import os
import shutil


LOG_DIR="logs"
QUARANTINE="quarantine"
BACKUP="backup"

def detect_suspicious_ips():
    try:
        attackers={}
        for root,dirs,files in os.walk(LOG_DIR):
            for f in files:
                with open(os.path.join(root,f)) as file:
                    for line in file:
                        parts=line.strip().split()
                        if len(parts)==3 and parts[2]=="failed":
                            ip=parts[0]
                            attackers[ip]=attackers.get(ip,0)+1
    except FileNotFoundError:
        print("file not found")
        return {}
    return attackers

def find_attackers(attacks_file,thresold=5):
    attackers=[]
    try:
        for ip,counts in attacks_file.items():
            if counts>=thresold:
                attackers.append(ip)
    except Exception as e:
        print("Error :",e)
        return []
    return attackers


def scan_files():
    try:
        malware=["malware.exe","virus.exe"]
        infected=[]
        for root,dirs,files in os.walk("system"):
            for f in files:
                if f in malware:
                    infected.append(os.path.join(root,f))
    except Exception as e:
        print("cannot find files",e)
        return []
    return infected


def quarantine_files(files):
    try:
        os.makedirs(QUARANTINE,exist_ok=True)
        for f in files:
            shutil.move(f,QUARANTINE)
            
    except Exception as e:
        print("Error :",e)

def backup_important():
    try:
        os.makedirs(BACKUP,exist_ok=True)
        for f in os.listdir("important"):
            shutil.copy(os.path.join("important", f), os.path.join(BACKUP, f))
            
    except Exception as e:
        print("Error :",e)
        
def save_result(files):
    try:
        with open("infected_files.txt","w") as f:
            for file in files:
                f.write(f"{file}\n")
    except:
        print("cannot save results")

def main():
    
    attacks=detect_suspicious_ips()
    
    attackers=find_attackers(attacks)
    print("Attack summary : ",attackers)
    
    infected=scan_files()
    print("INFECTED files : ",infected)
    
    if infected:
        quarantine_files(infected)
        save_result(infected)
        
    backup_important()
    
    
    
if __name__=="__main__":
    main()