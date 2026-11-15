def maximum_of_three_number(a, b, c):
    if a>=b and a>=c:
        print(f"{a} is Maximum Number")
    elif b>=a and b>=c:
        print(f"{b} is Maximum Number")
    else:
        print(f"{c} is Maximum Number")

maximum_of_three_number(12, 21, 13)