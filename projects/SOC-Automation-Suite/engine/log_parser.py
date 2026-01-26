def load_logs(path):
    logs = []
    try:
        with open(path) as f:
            for line in f:
                parts = line.strip().split()
                if len(parts) == 3:
                    ip, user, status = parts
                    logs.append({"ip": ip, "user": user, "status": status})
    except:
        pass
    return logs
