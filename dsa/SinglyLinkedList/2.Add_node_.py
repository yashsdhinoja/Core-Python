class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SLL:
    def __init__(self):
        self.head = None

# 
mylist = SLL()


node_1 = Node(10)
mylist.head = node_1 # 10

node_2 = Node(20)
node_1.next = node_2 # 10 -> 20

print(" ")
print(node_1.data,"->",node_2.data)
print(" ")
print("Node Memory Address : ", id(node_1))
print("Node Memory Address : ", id(node_2))
print(" ")
print("Node holds Second Node Address : ", id(node_1.next))