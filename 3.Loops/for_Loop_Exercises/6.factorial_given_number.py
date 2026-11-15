# Calculate and print the factorial of a given number.
# formula
# 5! = 5 x 4 x 3 x 2 x 1 = 120


def factorial_number(x):
    
    if x < 0:
        raise ValueError("Factorial is not defined for negative numbers.")

    result = 1
    for i in range(2, 1 + x):
        result *= i
    return result
    
        
print(factorial_number(int(input("Enter the + Number : "))))
