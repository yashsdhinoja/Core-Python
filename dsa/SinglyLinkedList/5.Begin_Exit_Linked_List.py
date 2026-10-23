class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SLL:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node

    def display(self):
        temp = self.head

        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


sll = SLL()

while True:
    print("\n1. Begin")
    print("0. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        n = int(input("Enter data: "))
        sll.insert(n)
        sll.display()

    elif choice == 0:
        print("Exit")
        break

    else:
        print("Invalid choice")
