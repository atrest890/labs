import math as m

a = 0
b = 1

def func(x):
    return x * x * m.sin(x)

def trapezium(a, b, n):
    h = (b - a) / n
    summ = (func(a) + func(b)) / 2
    for i in range(n-1):
        summ += func(a + i*h)
    I = h * summ
    return I

print("""
Численное интегрирование: метод трапеций
Определенный интеграл x^2 * sinx, [0;1]
""")


n = 6
print("При n = 6:")
ans = trapezium(a, b, n)
print("Ответ: {}".format(ans))

n = 12
print("При n = 12:")
ans = trapezium(a, b, n)
print("Ответ: {}".format(ans))

n = 60
print("При n = 60:")
ans = trapezium(a, b, n)
print("Ответ: {}".format(ans))

n = 600
print("При n = 600")
ans = trapezium(a, b, n)
print("Ответ: {}".format(ans))
