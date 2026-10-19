# Check whether the given number is a prime number.

# Flowchart Idea
# Plaintext
# Input Number (N)
#    │
#    ├── Is N <= 1? ───────────► YES ──► "Not Prime"
#    │
#    └── NO
#         │
#         ├── Set is_prime = True
#         │
#         ├── Loop 'i' from 2 to sqrt(N):
#         │     │
#         │     └── IF N % i == 0:
#         │           is_prime = False
#         │           Break loop
#         │
#         └── IF is_prime is True ──► "Prime Number"
#             ELSE ───────────────► "Not Prime"

num = int(input("Enter the Number : "))

if num > 1:
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
        if is_prime:
            print("Prime Number")
        else:
            print("1. Not a Prime Number")
else:
    print("2. Not a prime number")
    