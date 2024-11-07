"""Module providing a new function printing python version."""

# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

#Imports use here cuz not sure how to use functions in this file with no imports
from homeworks import find_substring
from homeworks import required_letter_h
from homeworks import check_person_age
from homeworks import check_length
from homeworks import show_strings

#task 1
""""Check quantity of arquments provided and type of data used"""
first_argument = "Goodbye"

def require_two_args(find_substring):
    if find_substring(first_argument, "somewords"):
        print("Only one argument given")

#print(require_two_args(find_substring))


def string_only_given(find_substring):
    if find_substring(int, list):
        pass
    else:
        print("Incorrect type, try string")


#string_only_given(find_substring)

#task 2
""""Check type of data of input and length of string"""
x = input()
def check_special_char_digit(required_letter_h):
    if required_letter_h(x.isdigit()) or required_letter_h(x.isascii()):
        print("String has digits or special characters")

#check_special_char_digit(required_letter_h)

def number_of_char(required_letter_h):
    if len(x) > 100:
        print("Too long string")
    else:
        print("Length is fine")

#number_of_char(required_letter_h)

#task 3
""""Check quantity of values and position of element age"""

lst3 = ["Joe", "Doe", 30, "Engineer", "Colombia"]
lst4 = []
def check_number_values(check_person_age):
    for value in lst3:
        if len(lst3) < 4:
            print("Missing data")

#check_number_values(check_person_age)

age = int
def check_age_position(check_person_age):
    for person in lst3:
        age = person[2]
        if type(age) != int:
            print("Wrong position or missing age data")
        break

#check_age_position(check_person_age)

#task 4
""""Check type of string data and case used"""
print("Enter your sentence")

def type_of_data(check_length):
    uniq_symbols = input()
    for c in uniq_symbols:
        if uniq_symbols.isdigit():
            print("Digit chars")
        elif not uniq_symbols.isalpha():
            print("Ascii chars")
        else:
            print("Alphabetic chars")
        break

#print(type_of_data(check_length))


def upper_case(check_length):
    uniq_symbols = input()
    for c in uniq_symbols:
        if c.isupper():
            print("Uppercase is used")
        elif c.islower():
            print("Lowercase is used")
        elif c.isspace():
            print("Space is used")
        break

#upper_case(check_length)

#task 5
""""Check quantity of not string elements in list and show them in lists"""
lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']

def quantity_of_values_not_str(show_strings):
    lst2 = []
    for word in lst1:
        if type(word) is str:
            lst2.append(word)
            result = (len(lst1)) - (len(lst2))
    print(f'"Quantity of elements not str type:" {result}')

#quantity_of_values_not_str(show_strings)

def show_int_and_bool(show_strings):
    lst3 = []
    lst4 = []
    for word in lst1:
        if type(word) is int:
            lst3.append(word)
        elif type(word) is bool:
            lst4.append(word)

    print(lst3, lst4)

#show_int_and_bool(show_strings)






# End-of-file (EOF)# End-of-file (EOF)
