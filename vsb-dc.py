while True:
    if input("press 1 for bin to denary ") == "1":
        try:
            print(int(input("enter binary number "), 2))
        except ValueError as ex:
            print("thats not binary bro")
    else:
        try:
            print(str(bin(int(input("enter denary number "))))[2:])
        except ValueError as ex2:
            print("Not a number my dude")
