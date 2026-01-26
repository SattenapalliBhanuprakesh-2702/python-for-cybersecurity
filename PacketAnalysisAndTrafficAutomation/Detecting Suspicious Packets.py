from scapy.all import rdpcap,DNSQR

packets=rdpcap("traffic.pcap")

for pkt in packets:
    if pkt.haslayer(DNSQR):
        qname=pkt[DNSQR].qname.decode(errors="ignore")
    if len(qname)>50:
        print("[SUSPICIOUS DNS]", qname)