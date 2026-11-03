def binarysearch(datatype, key):
    low = 0  # starting index
    high = len(datatype) - 1 # last index

    while low <= high:
        mid = (low + high) // 2 # middle index

        if datatype[mid] == key:
            return mid #return the index if found

        elif datatype[mid] < key:
            low = mid + 1

        else:
            high = mid - 1
    return -1 # element not found

datatype = [10, 20, 30, 40, 50]

key = int(input("Enter the element to search : "))

result = binarysearch(datatype, key)

if result == -1:
    print("Element not found")
else:
    print(f"Element found at index {result}")

    # works on sorted lists.
    