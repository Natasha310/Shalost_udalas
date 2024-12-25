"""Ітератори:
Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N."""
N = 50


def iter_even(N):
    for i in range(N):
       if i%2 == 0:
        print(i)

print(iter_even(N))

"""Реалізуйте ітератор для зворотного виведення елементів списку."""

list1 = [1,2,3]
def reversed_iter(list):
     for i in reversed(list):
         print(i)

print(reversed_iter(list1))

