# Syntax
# lambda arguments : expression

# 10 + 5 => 15
x = lambda a : a + 10
print(x(5))

# 2 + 6 => 8 
# 4 * 5 => 20
# 20 + 8 => final answer is 28
i = lambda s, k, l : s + k + l * 5
print(i(2, 6, 4))