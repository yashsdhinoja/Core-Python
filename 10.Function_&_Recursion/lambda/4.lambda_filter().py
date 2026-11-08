nums = [1,2,3,4,5,6,7,8,9,10]

for numbers in nums:
    if numbers % 2 == 0:
        print(f"Even : {numbers}", end=" ")
        Even_number = numbers**2
        print(f"Even : {Even_number}")
    else:
        print(f"Odd : {numbers}", end=" ")
        Odd_number = numbers**2
        print(f"Odd : {Odd_number}")
