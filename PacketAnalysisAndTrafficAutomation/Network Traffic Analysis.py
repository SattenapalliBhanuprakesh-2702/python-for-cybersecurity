from scapy.all import rdpcap,TCP,IP 

packets=rdpcap("traffic.pcap")
syn_count={}

for pkt in packets:
    if pkt.haslayer(TCP) and pkt[TCP].flags=="S":
        src=pkt[IP].src
        syn_count[src]=syn_count.get(src,0)+1
        
for ip,count in syn_count.items():
    if count>100:
        print("Alert possible port scan for :",ip)
        