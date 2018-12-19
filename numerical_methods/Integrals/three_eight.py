import math as m

a = 0
b = 1

def func(x):
    return x * x * m.sin(x)

def three_eight(a, b, n):
    h = (b-a) / (3*n)
    summ = func(a) + func(b)
    for i in range(3*n - 1):
        if i % 3 == 0:
            summ += 2*func(a + h*i)
        else:
            summ += 3*func(a + h*i)
            
    summ *= (3/8) * h
    return summ
 
print("""
Численное интегрирование: метод трех восьмых
Определенный интеграл x^2 * sinx, [0;1]
""")

 
n = 6
print("При n = 6:")
ans = three_eight(a, b, n)
print("Ответ: {0}".format(ans))

n = 12
print("При n = 12:")
ans = three_eight(a, b, n)
print("Ответ: {0}".format(ans))

n = 60
print("При n = 60:")
ans = three_eight(a, b, n)
print("Ответ: {0}".format(ans))

n = 600
print("При n = 600:")
ans = three_eight(a, b, n)
print("Ответ: {0}".format(ans))

