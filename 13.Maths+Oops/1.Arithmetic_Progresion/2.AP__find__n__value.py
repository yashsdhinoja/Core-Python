# create a AP (Arithmetic Progression) of nth term formula => [an = a + (n - 1) d].
# to find the n value formaula => [ ((an - ai) / d) + 1 ]

# class
class Arithmetic_Progression__Find__n:
    def __init__(self, a, n, d):
        self.a = a
        self.n = n
        self.d = d

    # method
    def n_th_term(self):
        if self.n is None:
            return "Please provide 'n' to find the n-th term."
        return self.a + (self.n - 1) * self.d

    def __n_th__(self, an):
        n_th = ((an - self.a) / self.d) + 1
        return int(n_th)

Arith_Progre = Arithmetic_Progression__Find__n(a=5, n=None, d=10)
print(Arith_Progre.__n_th__(85)) 

# n => 9