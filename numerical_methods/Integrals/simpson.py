import math as m

a = 0
b = 1

def func(x):
    return x * x * m.sin(x)

def simpson(a, b, n):
    h = (b - a) / n
    summ = func(a) + func(b)
    even = 0
    odd = 0
    for i in range(1, n-1):
        if i % 2 == 0:
            even += func(a + i*h)
        else:
            odd += func(a + i*h)
    summ += (2 * even + 4 * odd)
    I = (h/3) * summ
    return I

print("""
Численное интегрирование: метод Симпсона
Определенный интеграл x^2 * sinx, [0;1]
""")


n = 6
print("При n = 6:")
ans = simpson(a, b, n)
print("Ответ: {}".format(ans))

n = 12
print("При n = 12:")
ans = simpson(a, b, n)
print("Ответ: {}".format(ans))

n = 60
print("При n = 60:")
ans = simpson(a, b, n)
print("Ответ: {}".format(ans))

n = 600
print("При n = 600:")
ans = simpson(a, b, n)
print("Ответ: {}".format(ans))
