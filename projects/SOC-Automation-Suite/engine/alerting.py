from datetime import datetime

def generate_alerts(attacks, threat, packets):
    with open("siem.log", "a") as f:
        for ip, c in attacks.items():
            f.write(f"{datetime.now()} | BRUTEFORCE | {ip} | {c}\n")
        f.write(f"{datetime.now()} | NETWORK_THREAT_SCORE | {threat}\n")
        f.write(f"{datetime.now()} | SUSPICIOUS_PACKETS | {packets}\n")
