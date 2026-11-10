# create a AP (Arithmetic Progression) of nth term formula => [an = a + (n - 1) d].
# Use this when you have the first term, the position, and the common difference: an = a + (n - 1)d

# class
class Arithmetic_Progression:
    def __init__(self, a=5, n=9, d=10):  # parameter pass
        self.a = a
        self.n = n
        self.d = d

# method
    def find__an(self):
        an = self.a + (self.n - 1) * self.d
        return an

AP = Arithmetic_Progression()
print(AP.find__an())

# An => 85