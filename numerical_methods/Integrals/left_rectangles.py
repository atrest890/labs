import math as m

a = 0
b = 1

def func(x):
    return x * x * m.sin(x)

def leftRec(a, b, n):
    h = (b - a) / n
    summ = func(a)
    for i in range(n-1):
        summ += func(a + i*h)
    I = h * summ
    return I

print("""
Численное интегрирование: метод левых прямоугольников
Определенный интеграл x^2 * sinx, [0;1]
""")

n = 6
print("При n = 6:")
ans = leftRec(a, b, n)
print("Ответ: {0}".format(ans))

n = 12
print("При n = 12:")
ans = leftRec(a, b, n)
print("Ответ: {0}".format(ans))

n = 60
print("При n = 60:")
ans = leftRec(a, b, n)
print("Ответ: {0}".format(ans))

n = 600
print("При n = 600:")
ans = leftRec(a, b, n)
print("Ответ: {0}".format(ans))
