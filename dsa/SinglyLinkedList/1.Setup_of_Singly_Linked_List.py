class Node: # class blueprint
    def __init__(self, data): # constructor and pass parameter of data
        self.data = data
        self.next = None # Always starts as None, you have to link it later manually

# class Node:
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next  # Can accept a node right away, or default to None

class SLL:
    def __init__(self):
        self.head = None  # The list always starts empty, no matter what

# class SLL:
#     def __init__(self, head=None):
#         self.head = head  # The list can start empty OR start with an existing node

mylist = SLL()

first_node1 = Node(10)

mylist.head = first_node1

print("  ")
print(" | head data    |:", mylist.head.data)
print(" | Next Pointer |:", mylist.head.next)
#       INSPECTING DATA AND ADDRESSES
# print(" ===>>> INSPECTING DATA AND ADDRESSES <<<=== ")
# print(" Data inside Node 1     |: ", first_node1.data)
# print(" Memory Address of Node |: ", first_node1)