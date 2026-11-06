# create a AP (Arithmetic Progression) of nth term formula => [an = a + (n - 1) d].

class Arithmetic_Progression:
    def __init__(self, a=5, n=9, d=10):
        self.a = a
        self.n = n
        self.d = d

    def n_th_term(self):
        return self.a + (self.n - 1) * self.d
        

AP = Arithmetic_Progression()
print(AP.n_th_term())
