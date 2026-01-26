from scapy.all import rdpcap, IP, TCP, DNSQR, Raw
from datetime import datetime

PCAP = "traffic.pcap"
SCAN_THRESHOLD = 100

syn_tracker = {}
alerts = []

packets = rdpcap(PCAP)

for pkt in packets:
    if IP in pkt:
        src = pkt[IP].src

        # Port scan detection
        if pkt.haslayer(TCP) and pkt[TCP].flags == "S":
            syn_tracker[src] = syn_tracker.get(src, 0) + 1

        # DNS tunneling detection
        if pkt.haslayer(DNSQR):
            qname = pkt[DNSQR].qname.decode(errors="ignore")
            if len(qname) > 50:
                alerts.append(f"DNS TUNNELING from {src} | {qname}")

        # Suspicious HTTP tools
        if pkt.haslayer(Raw):
            payload = pkt[Raw].load.decode(errors="ignore")
            if "User-Agent" in payload:
                if "curl" in payload or "python" in payload:
                    alerts.append(f"SUSPICIOUS HTTP TOOL from {src}")

# Final scan alerts
for ip, count in syn_tracker.items():
    if count > SCAN_THRESHOLD:
        alerts.append(f"PORT SCAN from {ip} | SYNs={count}")

# SOC log
with open("soc_packet_alerts.log", "a") as f:
    for a in alerts:
        f.write(f"{datetime.now()} | {a}\n")

print("Packet analysis complete")
print("Alerts generated:", len(alerts))
