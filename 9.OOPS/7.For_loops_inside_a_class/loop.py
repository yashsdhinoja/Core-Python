class Loop:
    def __init__(self, number):
        self.number = number

    def straight(self):
        for i in range(1,int(self.number),1):
            print(i, end=" ")

    def reverse(self):
        print("\n")
        for j in range(int(self.number)-1,0,-1):
            print(j, end=" ")

L1 = Loop(11)
L1.straight()
L1.reverse()