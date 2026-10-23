class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SLL:
    def __init__(self):
        self.head = None

    def insert_last(self, data):
        new_node = Node(data)
        if self.head is None:
            print("Linkedlist empty")
            return
        else:
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            temp.next=new_node

    def insert_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_position(self,data,p):
        new_node=Node(data)
        temp=self.head
        for i in range(1,p-1):
            temp=temp.next
        new_node.next=temp.next
        temp.next=new_node

    def delete_begin(self):
        delete=self.head.data
        self.head=self.head.next
        print(delete," Node Deleted")   

    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    # def delete_value(self, value):


    # def search_value(self, value):


    # def count_value(self):

    
    # def reverse_operation(self):
    
s1 = SLL()
while True:
    print("0. Exit")
    print("1. Display")
    print("2. Insert at Begin")
    print("3. Insert at Last")
    print("4. Insert at Position")
    print("5. Delete at Begin")
    choice = int(input("Enter choice: "))
    if choice == 2:
        data=int(input("Enter Data="))
        s1.insert_begin(data)
    elif choice == 0:
        print("Exit")
        break
    elif choice == 1:
        s1.display()
    elif choice == 3:
        data=int(input("Enter Data="))
        s1.insert_last(data)
    elif choice == 4:
        p=int(input("Enter Position="))
        data=int(input("Enter Data="))
        s1.insert_position(data,p)
    elif choice == 5:
        s1.delete_begin()
    else:
        print("Invalid choice")
