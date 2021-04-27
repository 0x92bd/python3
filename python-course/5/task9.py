import math as m

"""
1- Assume you have the angle = 60, write a Python program to find:
a. sin(angle)
b. cos(angle)
c. tan(angle)
d. degrees(angle)
e. radians(angle)
"""
angle = 60
print("sin:", m.sin(angle))
print("cos:", m.cos(angle))
print("tan:", m.tan(angle))
print("degrees:", m.degrees(angle))
print("radians:", m.radians(angle))

"""
2- Assume you have the calculation result y = 98.34521, write a Python program to round this
result:
a. upwards to the nearest integer
b. downwards to the nearest integer
"""
y = 98.34521
print("round y upwards is:", m.ceil(y))
print("round y downwards is:", m.floor(y))

"""
3- Assume you have x = 7, write a Python program to find:
a. log(x)
b. e^x
c. x^3
d. The absolute value of x
e. The square root of x
"""
x = 7
print("log(x):", m.log(x))
print("e^x:", m.exp(x))
print("x^3:", m.pow(x, 3))
print("The absolute value of x:", m.fabs(x))
print("The square root of x:", m.sqrt(x))
