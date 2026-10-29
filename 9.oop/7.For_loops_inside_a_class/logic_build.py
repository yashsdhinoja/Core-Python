class NumberList:
    def __init__(self):
        self.numbers = []

    def fill(self, start, end):
        for i in range(start, end + 1):    # end + 1 so the last number is included
            self.numbers.append(i)

    def total(self):
        t = 0
        for n in self.numbers:
            t = t + n
            break

obj = NumberList()
obj.fill(1, 25)
print(obj.numbers)     # [1, 2, 3, ... 25]
print(obj.total())     # 325