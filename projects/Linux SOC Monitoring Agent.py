import subprocess
import shutil
from datetime import datetime

LOG_FILE = "soc_agent.log"


def get_processes():
    try:
        return subprocess.check_output(
            ["ps", "-eo", "pid,comm,%cpu,%mem"],
            text=True
        )
    except Exception as e:
        return f"PROCESS_ERROR: {e}"


def get_running_services():
    try:
        return subprocess.check_output(
            ["systemctl", "list-units", "--type=service", "--state=running"],
            text=True
        )
    except Exception as e:
        return f"SERVICE_ERROR: {e}"


def get_cron_jobs():
    try:
        return subprocess.check_output(
            ["crontab", "-l"],
            text=True
        )
    except subprocess.CalledProcessError:
        return "NO_CRON_JOBS"
    except Exception as e:
        return f"CRON_ERROR: {e}"


def get_users():
    try:
        users = []
        with open("/etc/passwd") as f:
            for line in f:
                users.append(line.split(":")[0])
        return ",".join(users)
    except Exception as e:
        return f"USER_ERROR: {e}"


def get_disk_usage():
    try:
        d = shutil.disk_usage("/")
        return round(d.used * 100 / d.total, 2)
    except Exception as e:
        return f"DISK_ERROR: {e}"


def log_event(event):
    try:
        with open(LOG_FILE, "a") as f:
            f.write(f"{datetime.now()} | {event}\n")
    except:
        pass


def main():
    log_event("SOC_AGENT_STARTED")

    disk_usage = get_disk_usage()
    log_event(f"DISK_USAGE_PERCENT={disk_usage}")

    users = get_users()
    log_event(f"USERS={users}")

    cron = get_cron_jobs()
    log_event(f"CRON_JOBS={cron}")

    services = get_running_services()
    log_event("RUNNING_SERVICES_COLLECTED")

    processes = get_processes()
    log_event("PROCESS_LIST_COLLECTED")

    log_event("SOC_AGENT_COMPLETED")


if __name__ == "__main__":
    main()
