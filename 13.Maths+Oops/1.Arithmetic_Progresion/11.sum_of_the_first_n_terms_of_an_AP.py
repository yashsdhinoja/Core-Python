#  the sum of the first n terms of an AP is given by => [ Sn = n/2 [2a + (n-1) d] ]
    
# class 
class Sum_numbers:
    def __init__(self, n=21, a=100, d=50):
        self.a = a
        self.d = d
        self.n = n
       
# method
    def Calculate_Sn(self):
        result = (self.n/2)*(2*self.a+(self.n-1)*self.d)
        return int(result)

Sn = Sum_numbers(n=21, a=100, d=50)
print(f"Sum of nums : {Sn.Calculate_Sn()}")