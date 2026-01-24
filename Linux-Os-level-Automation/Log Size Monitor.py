import os

def check_log_size(path="var/log"):
    alerts=[]
    for root,_,files in os.walk(path):
        for f in files:
            full=os.path.join(root,f)
            
            try:
                if os.path.getsize(full) > 50*1024*1024:
                    alerts.append(full)
            except:
                pass
    return alerts
            
alert_log=check_log_size()

for l in alert_log:
    print("Large log :",l)