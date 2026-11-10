# Use this when you know the n-th term, its position, and the common difference: ==>> [ a = an - (n - 1)d ]
# 2. To find the first term (a)Use this when you know the n-th term, its position, and the common difference:
# formula  =>  a = a_n - (n - 1)d

# class
class Arithmetic_Progression_a_:
    def __init__(self, a=None, d=10, n=4, an=5):
        self.a = a
        self.d = d
        self.n = n
        self.an = an
# method
    def a_th_find(self):
        if self.a is None:
            return "a is remaening."
        return self.a + (self.n - 1 ) * self.d

    def __a__(self):
        _a_ = self.an - (self.n - 1) * self.d
        return f"{_a_}"

ap_term = Arithmetic_Progression_a_(a=5,n=4,d=10)
print("The 4th term is:", ap_term.a_th_find())

ap_find__a__value = Arithmetic_Progression_a_(an=5, d=10, n=4)
print("The Position (a) is : ",ap_find__a__value.__a__())
