# 5.	Write a function to check whether a number is even or odd.
def odd_even(number):
    if number % 2 == 0:
        return "Number is even"
    else:
        return "Number is odd"

print(odd_even(3))
print(odd_even(8))