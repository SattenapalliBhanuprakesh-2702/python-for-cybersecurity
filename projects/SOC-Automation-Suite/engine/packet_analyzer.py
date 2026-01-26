from scapy.all import rdpcap, TCP, UDP

def analyze_pcap(path):
    suspicious = 0
    try:
        packets = rdpcap(path)
        for pkt in packets:
            if pkt.haslayer(TCP) or pkt.haslayer(UDP):
                if pkt.sport in [4444, 1337] or pkt.dport in [4444, 1337]:
                    suspicious += 1
    except:
        pass
    return suspicious
