def swap_XOR(a,b):
    print("Before Swap XOR^")
    print(" a :",a)
    print(" b :",b)

    a = a^b
    b = a^b
    a = a^b

    print("After Swap XOR^")
    print(" a :",a)
    print(" b :",b)
swap_XOR(10,20)
print("\n")