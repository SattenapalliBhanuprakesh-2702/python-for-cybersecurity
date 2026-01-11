username="Bhanu"
attempts=5
if attempts>3 and username=="Bhanu":
    print("Lock account")
elif attempts>3:
    print("show captcha")
else:
    print("login successful")