import subprocess

cmd = [
    "tshark",
    "-r", "traffic.pcap",
    "-T", "fields",
    "-e", "ip.src",
    "-e", "ip.dst",
    "-e", "dns.qry.name"
]

output = subprocess.check_output(cmd, text=True)

for line in output.splitlines():
    print(line)
