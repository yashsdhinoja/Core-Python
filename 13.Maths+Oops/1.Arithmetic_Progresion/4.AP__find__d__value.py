# Use this when you know the n-th term, the first term, and its position.
# formula to find d ==>> [ d = an - a / n - 1 ].

# class
class Arithmetic_Progression__Find__d:
    def __init__(self, a=5, n=9, d=None):
        self.a = a
        self.n = n
        self.d = d 

# method

    def __d__(self, an):
        d = (an - self.a) / (self.n - 1)
        return f"{d}"

    def d_th_term(self):
            if self.d is None:
                return "d is remening "
            return self.a + (self.n - 1) * self.d

ap_term = Arithmetic_Progression__Find__d(a=5, n=4, d=10)
print("The 4th term is:", ap_term.d_th_term())

ap_find__d__value = Arithmetic_Progression__Find__d(a=5, n=4)
print("The Position (d) for value 35 is :", ap_find__d__value.__d__(35))