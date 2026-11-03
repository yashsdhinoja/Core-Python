# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

# Doubly Linked List class
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # 1. Insert at beginning
    def insert_beginning(self, data):
        new_node = Node(data)

        new_node.next = self.head

        if self.head is not None:
            self.head.prev = new_node

        self.head = new_node

        print(data, "inserted at beginning.")

    # 2. Insert at end
    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            print(data, "inserted at end.")
            return

        temp = self.head

        while temp.next is not None:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

        print(data, "inserted at end.")

    # 3. Insert at specific position
    def insert_position(self, data, position):
        if position < 1:
            print("Invalid position.")
            return

        if position == 1:
            self.insert_beginning(data)
            return

        temp = self.head

        for i in range(1, position - 1):
            if temp is None:
                print("Invalid position.")
                return
            temp = temp.next

        if temp is None:
            print("Invalid position.")
            return

        new_node = Node(data)

        new_node.next = temp.next
        new_node.prev = temp

        if temp.next is not None:
            temp.next.prev = new_node

        temp.next = new_node

        print(data, "inserted at position", position)

    # 4. Delete from beginning
    def delete_beginning(self):
        if self.head is None:
            print("Linked list is empty.")
            return

        deleted_data = self.head.data
        self.head = self.head.next

        if self.head is not None:
            self.head.prev = None

        print(deleted_data, "deleted from beginning.")

    # 5. Delete from end
    def delete_end(self):
        if self.head is None:
            print("Linked list is empty.")
            return

        if self.head.next is None:
            deleted_data = self.head.data
            self.head = None
            print(deleted_data, "deleted from end.")
            return

        temp = self.head

        while temp.next is not None:
            temp = temp.next

        deleted_data = temp.data
        temp.prev.next = None

        print(deleted_data, "deleted from end.")

    # 6. Delete a node by value
    def delete_value(self, value):
        if self.head is None:
            print("Linked list is empty.")
            return

        temp = self.head

        while temp is not None:
            if temp.data == value:

                if temp.prev is not None:
                    temp.prev.next = temp.next
                else:
                    self.head = temp.next

                if temp.next is not None:
                    temp.next.prev = temp.prev

                print(value, "deleted from linked list.")
                return

            temp = temp.next

        print(value, "not found in linked list.")

    # 7. Search for an element
    def search(self, value):
        temp = self.head
        position = 1

        while temp is not None:
            if temp.data == value:
                print(value, "found at position", position)
                return

            temp = temp.next
            position += 1

        print(value, "not found in linked list.")

    # 8. Count the number of nodes
    def count_nodes(self):
        count = 0
        temp = self.head

        while temp is not None:
            count += 1
            temp = temp.next

        print("Total number of nodes:", count)

    # 9. Reverse the linked list
    def reverse(self):
        if self.head is None:
            print("Linked list is empty.")
            return

        current = self.head
        previous = None

        while current is not None:
            previous = current.prev
            current.prev = current.next
            current.next = previous
            current = current.prev

        self.head = previous.prev

        print("Linked list reversed.")

    # 10. Display in forward direction
    def display(self):
        if self.head is None:
            print("Linked list is empty.")
            return

        temp = self.head

        print("Forward:", end=" ")

        while temp is not None:
            print(temp.data, end=" <-> ")
            temp = temp.next

        print("None")

    # 11. Display in backward direction
    def display_backward(self):
        if self.head is None:
            print("Linked list is empty.")
            return

        temp = self.head

        while temp.next is not None:
            temp = temp.next

        print("Backward:", end=" ")

        while temp is not None:
            print(temp.data, end=" <-> ")
            temp = temp.prev

        print("None")


# Main Program
linked_list = DoublyLinkedList()

while True:
    print("\n======= DOUBLY LINKED LIST =======")
    print("1. Insert at Beginning")
    print("2. Insert at End")
    print("3. Insert at Specific Position")
    print("4. Delete from Beginning")
    print("5. Delete from End")
    print("6. Delete by Value")
    print("7. Search an Element")
    print("8. Count Nodes")
    print("9. Reverse Linked List")
    print("10. Display Forward")
    print("11. Display Backward")
    print("12. Exit")
    print("==================================")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if choice == 1:
        data = int(input("Enter data: "))
        linked_list.insert_beginning(data)

    elif choice == 2:
        data = int(input("Enter data: "))
        linked_list.insert_end(data)

    elif choice == 3:
        data = int(input("Enter data: "))
        position = int(input("Enter position: "))
        linked_list.insert_position(data, position)

    elif choice == 4:
        linked_list.delete_beginning()

    elif choice == 5:
        linked_list.delete_end()

    elif choice == 6:
        value = int(input("Enter value to delete: "))
        linked_list.delete_value(value)

    elif choice == 7:
        value = int(input("Enter value to search: "))
        linked_list.search(value)

    elif choice == 8:
        linked_list.count_nodes()

    elif choice == 9:
        linked_list.reverse()

    elif choice == 10:
        linked_list.display()

    elif choice == 11:
        linked_list.display_backward()

    elif choice == 12:
        print("Program terminated.")
        break

    else:
        print("Invalid choice. Please try again.")
