failed_logins=7
if failed_logins>10:
    print("critical")
elif failed_logins>5:
    print("high")
else:
    print("low")