def arithmetic_opertion(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b

a = int(input("Enter the a Value : "))
b = int(input("Enter the b Value : "))

print(f"Before a = {a} and b = {b}".format(a,b))

a, b = arithmetic_opertion(a,b)

print(f"After : a = {a}, b = {b}".format(a,b))