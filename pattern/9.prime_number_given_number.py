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