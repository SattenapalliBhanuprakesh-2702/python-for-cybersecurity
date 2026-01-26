from scapy.all import rdpcap,IP,TCP,UDP,DNS

packets=rdpcap('traffic.pcap')
for pkt in packets:
    if IP in pkt:
        print(pkt[IP].src,"->",pkt[IP].dist)