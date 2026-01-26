from scapy.all import rdpcap,RAW

packets=rdpcap("traffic.pcap")
for pkt in packets:
    if pkt.haslayer(RAW):
        payload=pkt[RAW].load.decoed(errors="ignore")
        if "User-Agent" in payload:
            if "curl" in payload or "python" in payload:
                print("suspicious user-agent :",payload.split("\n")[0])
                
                