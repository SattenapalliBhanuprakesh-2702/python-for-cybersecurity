import shutil
import subprocess

def system_health():
    cpu=subprocess.check_output(["uptime"],text=True).strip()
    disk=shutil.disk_usage("/")
    return {
        "cpu":cpu,
        "disk_used_percent":disk.used*100/disk.total
    }
    
health=system_health()
print(health)