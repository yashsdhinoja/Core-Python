class Node: #1:40
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DLL:
    def __init__(self):
        self.head = None

    def insert_begin(self,data):
        new_node = Node(data)
        new_node.next=self.head
        if self.head is not None:
            print("Yes")

L1 = DLL()

while True:
    print("1. Insert Begin ")
    print("2. Insert End ")
    print("3. Delete Begin ")
    print("4. Delete End ")
    print("5. Display ")
    print("6. End ")