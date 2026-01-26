def detect_bruteforce(logs, threshold=5):
    counter = {}
    for log in logs:
        if log["status"] == "failed":
            ip = log["ip"]
            counter[ip] = counter.get(ip, 0) + 1
    return {ip: c for ip, c in counter.items() if c >= threshold}
