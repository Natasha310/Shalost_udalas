"""Module providing a new function printing python version."""




#task 1
def find_substring(str1, str2):
    if str2 in str1:
        print(str1.index(str2))
    else:
        return -1


str1 = "Hello, world!"
str2 = "world"

print(find_substring(str1, str2))

#task 2
def required_letter_h(str3):

    for i in str3.lower():
        if "h" in str3.lower():
            print("Success")
        else:
            print("Enter char H/h to complete")
            str3()
        return

print(required_letter_h("ghj"))

#task 3
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

#task 4
def check_length(input):
    print("Enter your sentence")
    uniq_symbols = input()
    for c in uniq_symbols:
        if len(set(uniq_symbols.lower())) >= 10:
            print(True)
        else:
            print(False)
        break

print(check_length(input))
#task 5

lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
def show_strings(list):
    lst2 = []
    for word in lst1:
        if type(word) is str:
            lst2.append(word)

    print(lst2)

print(show_strings(lst1))


# End-of-file (EOF)# End-of-file (EOF)
