"""Module providing a new function printing python version."""




# task 1
#/""" Задача - надрукувати табличку множення на задане число, але
#лише до максимального значення для добутку - 25.
#Код майже готовий, треба знайти помилки та випраавити\доповнити."""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while multiplier <= number:
        result = number * multiplier
        # десь тут помила, а може не одна
        if  result > 25:
            break
            # Enter the action to take if the result is greater than 25
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        multiplier += 1



print(multiplication_table(3))
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
#"""  Написати функцію, яка обчислює суму двох чисел.
#"""
def sum_of_numbers(arg1, arg2):
    return arg1+arg2

amount = sum_of_numbers(6,6)
print(amount)
# task 3
#"""  Написати функцію, яка розрахує середнє арифметичне списку чисел."""
numbers = [3,4,5]
def middle_number(n):
    avarage = sum(n) / len(n)
    return avarage

av_number = middle_number(numbers)
print(av_number)
# task 4
#"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку."""
def reverse_string(s):
    return s[::-1]
revers = reverse_string("new string line")
print(revers)

# task 5
#"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку."""

def longest_word(lst1):
    return max(lst1, key=len)

lst2 = ["my", "first", "line"]
words = longest_word(lst2)
print(words)

# task 6
#"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
#у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
#не є підрядком першого рядка."""

def find_substring(str1, str2):
    if str2 in str1:
        print(str1.index(str2))
    else:
        return -1


str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7
def required_letter_h(str3):

    for i in str3.lower():
        if "h" in str3.lower():
            print("Success")
        else:
            print("Enter char H/h to complete")
            str3()
        return

print(required_letter_h("ghj"))
# task 8
lst3 = []
def show_only_string(arg4):
    if type(arg4) is str:
        lst3.append(arg4)
    else:
        print("Wrong type, try string type!")
    return lst3

print(show_only_string("88"))
# task 9
people_records = [
  ('John', 'Doe', 28, 'Engineer', 'New York'),
  ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
  ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),]

def check_person_age(list):
    for person in list:
        age = person[2]
        if age < 30:
            print("You can pass!")
        break

print(check_person_age(people_records))
# task 10

def swap_list(list):

    swapped_l = list[0], list[1] = list[1], list[0]
    return swapped_l

print(swap_list(people_records))

#"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
#перетворіть їх у 4 функції, що отримують значення та повертають результат.
#Обоязково документуйте функції та дайте зрозумілі імена змінним."""



# End-of-file (EOF)# End-of-file (EOF)

