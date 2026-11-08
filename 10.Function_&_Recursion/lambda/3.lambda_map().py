nums = [1,2,3,4,5,6,7,8,9,10]
squares = list(map(lambda x:x ** 2, nums))
even = list(map(lambda x: x % 2 == 0, nums))
odd = list(map(lambda x:x % 2 != 0, nums))

print(f"Squares : {squares}\n")
print(f"Even : {even}\n")
print(f"Odd : {odd}\n")

# Squares : [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# Even : [False, True, False, True, False, True, False, True, False, True]
# Odd : [True, False, True, False, True, False, True, False, True, False]