# 8.	Write a function to calculate the area of a circle.
import math

def Area_Circle(radius:float):
    if radius < 0:
        raise ValueError("Error")
    return math.pi * (radius**2)

print(Area_Circle(4))