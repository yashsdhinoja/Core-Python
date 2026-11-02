class tables:
    def __init__(self, number):
        self.number = number

    def multiplication(self):
        for i in range(1, 11):
            print(f"{self.number} x {i} = {self.number * i}")

TT = tables(4)
TT.multiplication()