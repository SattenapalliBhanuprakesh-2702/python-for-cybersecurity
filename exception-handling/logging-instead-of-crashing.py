try:
    file=open("secure.log")
    data=file.read()
    print(data)
except Exception as e:
    with open("error.log","a") as log:
        log.write(str(e)+"\n")