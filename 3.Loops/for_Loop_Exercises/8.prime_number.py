# print all prime numbers between 1 to 100.
# Loop 'num' from 2 to 100:
#    │
#    ├── Set is_prime = True
#    │
#    ├── Loop 'i' from 2 up to num - 1:
#    │     │
#    │     └── IF num % i == 0:
#    │           is_prime = False
#    │           Break loop
#    │
#    └── IF is_prime is True:
#          Print num

for num in range(2, 100, 1):
    is_prime = True
    for i in range(2, num-1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime is True:
        print(num, end=" ")

# output ==>> 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 