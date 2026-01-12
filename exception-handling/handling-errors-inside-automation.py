def load_logs(file):
    try:
        with open(file) as f:
            return f.readlines()
    except:
        print("cannot read the log file")
        return []
    
print(load_logs("auth.log"))