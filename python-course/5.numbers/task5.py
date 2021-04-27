a, b, c = False, True, True
q = (a and b) or ((b or c) and (b and c))
print("Question 1", q)

a = False
print("Question 2", not a)
