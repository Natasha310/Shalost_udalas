
"""Генератори:
Напишіть генератор, який повертає послідовність парних чисел від 0 до N.
Створіть генератор, який генерує послідовність Фібоначчі до певного числа N."""

class Generator:
    def __init__(self, N):
        self.N = N
        self.result = None


    def __iter__(self):
        self.result = (itm for itm in range(self.N) if itm % 2 == 0)
        return self.result


gener = Generator(10)
for itm in gener:
    print(itm)


class Fibonachi:
    def __init__(self, N):
         self.N = N


    def __iter__(self):
        a, b = 0, 1
        while b <= self.N:
            yield b
            a, b = b, a + b


f = Fibonachi(10)
for i in f:
    print(i)
