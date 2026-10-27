# print the fibonacci series up to the required number of terms.

nterms = int(input("Enter the Number : "))
n1, n2 = 0, 1
count = 0

if nterms <= 0:
    print("Enter the Positive Number.")
elif nterms == 1:
    print(f"Fibonacci Series {nterms} .")
    print(n1)
else:
    while count < nterms:
        print(n1, end=" ")
        nth = n1+ n2
        n1 = n2
        n2 = nth
        count += 1