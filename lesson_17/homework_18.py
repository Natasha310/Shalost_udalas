
"""Генератори:
Напишіть генератор, який повертає послідовність парних чисел від 0 до N."""

N = 50
even_gener = (itm for itm in range(10) if itm%2 == 0)
for itm in even_gener:
    print("itm")

"""Створіть генератор, який генерує послідовність Фібоначчі до певного числа N."""

def gen_fib(N):
    a, b = 0, 1
    while b <= N:
        yield b
        a, b = b, a + b

f = gen_fib(N)
for i in f:
    print(i)



