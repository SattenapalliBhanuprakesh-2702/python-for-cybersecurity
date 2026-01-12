try:
    file=open("auth.log")
    print(file.read())
except FileNotFoundError:
    print("log file not found")