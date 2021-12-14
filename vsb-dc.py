while True:
    if input("press 1 for bin to dec ") == "1":
        try:
            print(int(input("enter binary number "), 2))
        except ValueError as ex:
            print("thats not binary bro")
    else:
        print(bin(int(input("enter denary number "))))
