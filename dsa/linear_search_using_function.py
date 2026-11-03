def linearsearch(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1
#       0   1   2   3   4   5
arr = [10, 20, 30, 40, 50, 60]
key = int(input("Enter the element to search : "))

result = linearsearch(arr, key)

if result == -1:
    print("Element not found")
else:
    print("Element found at index",result)

# >>>>>>> return i <<<<<<<

# returns the value.
# can store in a variable.
# Useful for further calculations.

# >>>>>>> print(f"{i}") <<<<<<<

# displays the  value.
# cannot store the returned index.
# useful for displaying output.