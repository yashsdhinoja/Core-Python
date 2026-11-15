# 1.
# Parameters and Arguments.
# Parameters are the variable listed in the function definition.
# Arguments are the values passed to the function when it is called.

def add(a,b):
    return a + b
result = add(5,7) # Arguments passed
print(f"Parameters and Arguments : {result}") # output :- 12

def addition(c,f):
    return c * f # 5 x 9 'OR' 3 x 4
print(addition(5,9)) # output :- 45
reult2 = addition(3,4) # Arguments passed
print(reult2) # output :- 12

# 2.
# Return Statement:
# The return statement ends the function and sends a result back to the caller.
print("Return Statement")
def square(x):
    return x * x # 4 * 4
print(square(4)) # output :- 16

# 3.
# Default Parameters:
# you can provide default values for parameters.
print("Default Parameters")
def greet(name, msg="Hello"):
    return msg + ", " + name
print(greet("Alice"))
print(greet("Bob","hi"))