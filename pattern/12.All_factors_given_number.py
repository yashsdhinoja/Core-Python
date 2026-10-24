#

def all_factors_given_number(num):
    print(f"Factors number are {num}")
    for i in range(1, num + 1):
        if num % i == 0:
            print(i, end=" ")
    print("")

number = int(input("Enter the Number : "))
all_factors_given_number(number)

