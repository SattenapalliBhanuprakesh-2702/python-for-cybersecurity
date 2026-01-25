
def list_users():
    with open("etc/passwd") as f:
        user=[]
        for line in f:
            part=line.split(":")
            user.append(part[0])
    return user

def list_sudo_user():
    with open("etc/group") as f:
        sudo=[]
        for line in f:
            if line.startswith("sudo"):
                sudo=line.strip().split(":")[-1].split(",")
        return sudo
    

print("Users :",list_users())
print("Sudo Users :",list_sudo_user())
