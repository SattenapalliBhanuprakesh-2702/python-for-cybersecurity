try:
    attacks=10
    time=0
    rate=attacks/time
    print("rate of attacks:",rate)
except ZeroDivisionError:
    print("Cannot calculate attackrate")
    