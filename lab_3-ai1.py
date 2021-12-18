from random import random
A = [random() * 10 for x in range(7)]
print("Дійсні числа:")
for i in range (7):
    print("a", i, " = ", A[i])
def p(y):
    result = 0
    for i in range (7):
        result += A[i] * (y ** i)
    return result
for x in (1, 3, 4):
    result = p(x + 1) - p(x)
    print("Для x = ", x, ": p(x + 1) - p(x) = ", result)