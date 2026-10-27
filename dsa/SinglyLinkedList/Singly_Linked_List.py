
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
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node

    def insert_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_position(self, data, p):
        if p < 1:
            print("Invalid Position")
            return

        new_node = Node(data)
        if p == 1:
            new_node.next = self.head
            self.head = new_node
            return
        temp = self.head

        for i in range(1, p - 1):
            if temp is None:
                print("Invalid Position")
                return
            temp = temp.next

        if temp is None:
            print("Invalid Position")
            return

        new_node.next = temp.next
        temp.next = new_node

    def delete_begin(self):
        if self.head is None:
            print("Linked List is empty")
            return

        delete = self.head.data
        self.head = self.head.next
        print(delete, "Node Deleted")

    def display(self):
        if self.head is None:
            print("Linked List is empty")
            return

        temp = self.head

        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")

s1 = SLL()

while True:
    print("\n0. Exit")
    print("1. Display")
    print("2. Insert at Begin")
    print("3. Insert at Last")
    print("4. Insert at Position")
    print("5. Delete at Begin")

    choice = int(input("Enter choice: "))

    if choice == 2:
        data = int(input("Enter Data: "))
        s1.insert_begin(data)

    elif choice == 0:
        print("Exit")
        break

    elif choice == 1:
        s1.display()

    elif choice == 3:
        data = int(input("Enter Data: "))
        s1.insert_last(data)

    elif choice == 4:
        p = int(input("Enter Position: "))
        data = int(input("Enter Data: "))
        s1.insert_position(data, p)

    elif choice == 5:
        s1.delete_begin()

    else:
        print("Invalid choice")
