def load_logs(auth):
    try:
        logs=[]
        with open(auth) as a:
            for line in a:
                parts=line.strip().split()
                
                if len(parts)!=3:
                    continue
                
                ip,user,status=parts
                logs.append(
                    {
                        "ip":ip,
                        "user":user,
                        "status":status
                    }
                )
        return logs
    except FileNotFoundError:
        print("log file is empty")
        return []
    
def detect_attacks(logs):
    try:
        counter={}
        for log in logs:
            if log["status"]=="failed":
                ip=log["ip"]
                counter[ip]=counter.get(ip,0)+1
        return counter
    except:
        print("detection engine fail")
        return {}

def save_result(data):
    try:
        with open("results.txt","w") as f:
            f.write("  ip Address | Failed Attempts")
            f.write("\n")
            f.write("-----------------------------")
            f.write("\n")
            for ip,count in data.items():
                f.write(f'{ip}     |    {count}   \n')
                
    except:
        print("cannot save results")
        
def main():        
    logs=load_logs("auth.log")
    attackers_data=detect_attacks(logs)
    save_result(attackers_data)
    
if __name__=="__main__":
    main()