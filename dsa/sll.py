class node:
    def __init__(self, data):
        self.data = data
        self.next = None
class sll:
    def __init__(self):
        self.head = None
        new_node = node(10)

    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next

    def insert_start(self, data):
        newnode = node(data)
        newnode.next = self.head
        self.head = newnode

    def insert_end(self,data):
        newnode = node(data)
        if self.head  is None:
            self.head = newnode
            return 
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = newnode

    def insert_position(self,data,pos):
        if pos < 0:
            print('invalid position')
            return
        if pos == 1:
            self.insert_start(data)
            return
        temp = self.head
        for i in range(pos-2):
            if temp is None:
                print('invalid position')
                return
            temp = temp.next

        if temp is None:
            print('invalid position')
            return 

        newnode = node(data)
        newnode.next = temp.next
        temp.next = newnode

    def delete_start(self):
        if self.head is None:
            print('list is empty')
            return
        self.head = self.head.next

    def delete_end(self):
        if self.head is None:
            print('list is empty ')
            return 
        if self.head.next is None:
            self.head = None
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = None

    # def deletefromnumber(self,number):
        # if pos < 0 or self.head is None:
        #     print('invalid position or empty list ')
        #     return
        # if pos == 1:
        #     self.delete_start()
        #     return
        # temp = self.head
        # for i in range(pos-2):
        #     if temp is None:
        #         print('invalid position')
        #         return
        #     temp = temp.next
        #     if temp is None or temp.next is None:
        #         print('invalid position')
        #         return
        #     temp.next = temp.next.next

        #delete from number 



l1 = sll()
l1.insert_start(10)
l1.insert_start(20)

l1.display()
