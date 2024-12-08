"""Ітератори:
1.Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N.
2.Реалізуйте ітератор для зворотного виведення елементів списку."""

class Iterator:
    def __init__(self, N):
        self.N = N

    def __iter__(self):
        for i in range(self.N):
           if i%2 <= 0:
            yield i



iterat1 = Iterator(50)
for el in iterat1:
    print(el)


class Reverse:
    def __init__(self, list1):
        self.list1 = list1

    def __iter__(self):
         for itm in reversed(self.list1):
             yield itm

    def __next__(self):
        while True:
            item = next(self.list1, "end")
            if item == "end":
                break
            print(item)





iterat2 = Reverse([1,2,3])
for r in iterat2:
     print(r)
