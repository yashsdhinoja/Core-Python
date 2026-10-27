# Calculate and print the factorial of every number from 1 to n.
# formula
# 5! = 5 x 4 x 3 x 2 x 1 = 120

def factorial_number_counter(x):
    if x < 0:  # to see whether number is Negative or Not
        raise ValueError("Factorial is not defined for negative numbers.")
    
    factorial_add = 1 # to push the number
    for i in range(1, 1 + x): 
        factorial_add *= i # ex:- 5! = 5 x 4 x 3 x 2 x 1 = 120
        if factorial_add % 2 == 0:
            print(f"{i}! x {factorial_add} is Even Number ")
        else:
            print(f"{i}! x {factorial_add} is Odd Number ")

print(factorial_number_counter(int(input("Enter the Positive Number : "))))