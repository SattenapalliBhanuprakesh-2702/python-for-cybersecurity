import subprocess

def service_status(service):
    try:
        result = subprocess.check_output(["systemctl", "is-active", service], text=True)
        return result.strip()
    except:
        return "unknown"

services = ["ssh", "cron", "apache2"]

for s in services:
    print(s, service_status(s))
