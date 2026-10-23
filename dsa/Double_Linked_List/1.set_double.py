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
            self.head.prev=new_node
        self.head=new_node

    def insert_Last(self,data):
        new_node = Node(data)

    def Insert_Specific_Position(self, data, position, number):
        new_node = Node(data)
        if self.head is None:
            print("LinkedList is Empty")
            return
        
        temp = self.head
        for i in range(1, position-1):
            if temp is not None:
                print("invalid position")
                return
        new_node.next=new_node
        new_node.   



    def display(self):
        temp=self.head
        while temp is not None:
            print(temp.data, end="<->")
            temp=temp.next
        print("None")

d1 = DLL()

while True:
    print("1. Insert at Begin")
    print("2. Insert at Last")
    print("3. Insert at Specific Position")
    print("4. Delete at Begin")
    print("5. Delete at Last")
    print("6. Delete by Value")
    print("7. Count Node")
    print("8. Search Node")
    print("9. Reverse Linked List")
    print("10. Display Linked List")
    print("11. Exit")
    choice = int(input("Enter choice="))
    if choice == 1:
        data=int(input("Enter data="))
        d1.insert_begin(data)
    elif choice == 2:
        data=int(input("Enter data="))
        d1.insert_Last(data)
    elif choice == 3:
        data=int(input("Enter data="))
        d1.Insert_Specific_Position(data)
    elif choice == 4:
        break
    elif choice == 5:
        break
    elif choice == 6:
        break
    elif choice == 7:
        break
    elif choice == 8:
        break
    elif choice == 9:
        break
    elif choice == 10:
        d1.display()
    elif choice == 11:
        break
    else:
        print("Invalid choice")
