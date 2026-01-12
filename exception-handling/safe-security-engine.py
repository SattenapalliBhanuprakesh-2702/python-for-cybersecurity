def load_logs(filename):
    logs = []

    try:
        with open(filename, "r") as file:
            for line in file:
                parts = line.strip().split()

                if len(parts) != 3:
                    continue

                ip, user, status = parts
                logs.append({
                    "ip": ip,
                    "user": user,
                    "status": status
                })

    except FileNotFoundError:
        print("Log file not found")

    return logs


def detect_attacks(logs):
    counter = {}

    try:
        for log in logs:
            if log["status"] == "failed":
                ip = log["ip"]
                counter[ip] = counter.get(ip, 0) + 1

    except Exception as e:
        print("Detection error:", e)

    return counter


def save_results(data):
    try:
        with open("results.txt", "w") as f:
            f.write("IP Address | Failed Attempts\n")
            f.write("----------------------------\n")

            for ip, count in data.items():
                f.write(f"{ip} | {count}\n")

    except Exception as e:
        print("Cannot save results:", e)


def main():
    logs = load_logs("auth.log")
    attack_data = detect_attacks(logs)
    save_results(attack_data)


if __name__ == "__main__":
    main()
