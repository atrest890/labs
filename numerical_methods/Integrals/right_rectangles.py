import math as m

a = 0
b = 1

def func(x):
    return x * x * m.sin(x)

def rightRec(a, b, n):
    h = (b - a) / n
    summ = func(b)
    for i in range(1, n):
        summ += func(b - i*h)
    I = h * summ
    return I

print("""
Численное интегрирование: метод правых прямоугольников
Определенный интеграл x^2 * sinx, [0;1]
""")

n = 6
print("При n = 6:")
ans = rightRec(a, b, n)
print("Ответ: {0}".format(ans))

n = 12
print("При n = 12:")
ans = rightRec(a, b, n)
print("Ответ: {0}".format(ans))

n = 60
print("При n = 60:")
ans = rightRec(a, b, n)
print("Ответ: {0}".format(ans))

n = 600
print("При n = 600:")
ans = rightRec(a, b, n)
print("Ответ: {0}".format(ans))
