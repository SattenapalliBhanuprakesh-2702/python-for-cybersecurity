import subprocess

def list_process():
    
    try:
         #windows
        process = subprocess.check_output(  
            ["tasklist"],
            text=True
        )

        process=subprocess.check_output(["ps","-eo","pid,comm,%cpu,%mem"],text=True) #for linux
        return process.splitlines()[1:]
    except Exception:
        return []
    
def detect_suspicious(processlist):
    suspicious=[]
    for p in processlist:
        p_lower=p.lower()
        if "python" in p_lower or "nc" in p_lower or "bash" in p_lower:
            suspicious.append(p)
    return suspicious

processes=list_process()
alerts=detect_suspicious(processes)

for a in alerts:
    print(a,"\n")