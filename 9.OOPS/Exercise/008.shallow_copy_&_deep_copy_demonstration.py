# Demonstrate the different between a shallow copy and a deep copy using a class that contains a mutable list attribute.
import copy

class Test:
    def __init__(self, member):
        self.member = member

Original = Test(["Alex", "Bobs"])
Shallow = copy.copy(Original)
deep = copy.deepcopy(Original)

Shallow.member.append("cherry")  # add 1 members manually

print(f"Original  =>  {Original.member}")
print(f"Shallow   =>  {Shallow.member}")
print(f"Deep      =>  {deep.member}")

# Original  =>  ['Alex', 'Bobs', 'cherry']
# Shallow   =>  ['Alex', 'Bobs', 'cherry']
# Deep      =>  ['Alex', 'Bobs']