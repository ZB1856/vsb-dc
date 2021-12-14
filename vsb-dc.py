while True:
    if input("press 1 for bin to denary, anything else is denary to binary ") == "1":
        try:
            print(int(input("enter binary number "), 2))
        except ValueError as ex:
            print("thats not binary bro")
    else:
        try:
            thing1 = int(input("enter denary number "))
            eggs = str(bin(int(thing1)))[2:]
            print(eggs)
            if thing1 <= 255:
                print(f"8bit: {('0'*(8-len(eggs)))}{eggs}")
        except ValueError as ex2:
            print("Not a number my dude")
            
