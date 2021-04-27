"""
1- Write a Python program to calculate the area of a trapezoid.
         Height: 5
         Base, first value: 5
         Base, second value: 6
"""
base_1, base_2, height = 7, 8, 9
area = ((base_1 + base_2) / 2) * height
print(area)

"""
2- Can you guess, what is the result of the following expression?
 (a * (b % c)) + (q / d)
Where: a = 10, b = 45, c =4, q = 23, v =19, d = 11
"""
# a = 10; b = 45; c =4; q = 23; v =19; d = 11
a, b, c, q, v, d = 10, 45, 4, 23, 19, 11
result = (a * (b % c)) + (q / d)
print(result)
