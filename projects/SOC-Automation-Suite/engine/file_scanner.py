import os, shutil

def scan_files(root, bad_names):
    infected = []
    for root,dir,files in os.walk(root):
        for name in files:
            if name in bad_names:
                infected.append(os.path.join(root, name))
    return infected

def quarantine_files(files):
    os.makedirs("quarantine", exist_ok=True)
    for f in files:
        try:
            shutil.move(f, "quarantine")
        except:
            pass

def backup_files(files):
    os.makedirs("backup", exist_ok=True)
    for f in files:
        try:
            shutil.copy(f, "backup")
        except:
            pass
