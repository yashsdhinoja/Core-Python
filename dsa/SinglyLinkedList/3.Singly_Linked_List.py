class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SLL:
    def __init__(self):
        self.head = None

    # Insert Data into Single_Linked_List 
    def insert(self,data):
        new_node = Node(data) # New Node 

        if self.head is None: # head is emppty then insert new data
            self.head = new_node # head is empty new data is inserted
            return

        temp = self.head # temp is var because head is not moved once is go next node it can't reverse (come back to first node).
        while temp.next != None:
            temp = temp.next # push to next node

    # Display the Linked_List 
    def display(self):
        temp = self.head
        while temp != None:
            print(temp.data)
            temp = temp.next

L1 = SLL()

L1.insert(10)

L1.display()