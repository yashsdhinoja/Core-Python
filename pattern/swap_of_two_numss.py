def swap_num(a, b):
    temp = a
    a = b
    b = temp
    return a, b 

num1 = int(input("Enter the a Value : "))
num2 = int(input("Enter the b Value : "))
print(f"Before: num 1 = {num1} and num 2 = {num2}". format(num1, num2))
a, b = swap_num(num1, num2)
print(f"After : num 1 = {a} and num 2 = {b}". format(a,b))