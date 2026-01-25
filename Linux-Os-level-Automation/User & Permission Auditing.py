
def list_users():
    user=[]
    with open("/etc/passwd") as f:
        for line in f:
            part=line.split(":")
            user.append(part[0])
    return user

def list_sudo_user():
    sudo=[]
    with open("/etc/group") as f:
        for line in f:
            if line.startswith("sudo"):
                sudo=line.strip().split(":")[-1].split(",")
        return sudo
    

print("Users :",list_users())
print("Sudo Users :",list_sudo_user())
