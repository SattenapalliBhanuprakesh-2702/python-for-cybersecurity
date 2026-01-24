import subprocess

def cron_list():
    
    try:
        output=subprocess.check_output(["crontab","-l"],text=True)
        return output.strip()
    except:
        return ""
    
cron=cron_list()
print(cron)