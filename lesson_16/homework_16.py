# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring


"""Завдання 1
Створіть клас Employee, який має атрибути name та salary. Далі створіть два класи, Manager та Developer,
які успадковуються від Employee. Клас Manager повинен мати додатковий атрибут department, а клас Developer -
атрибут programming_language.
Тепер створіть клас TeamLead, який успадковується як від Manager, так і від Developer. Цей клас представляє
керівника з
команди розробників. Клас TeamLead повинен мати всі атрибути як Manager (ім''я, зарплата, відділ),
а також атрибут
team_size, який вказує на кількість розробників у команді, якою керує керівник.
Напишіть тест, який перевіряє наявність атрибутів з Manager та Developer у класі TeamLead"""


class Employee:
    def __init__(self, name, salary, **kwargs):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        self.department = department
        Employee.__init__(self, name, salary)

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        self.programming_language = programming_language
        Employee.__init__(self, name, salary)


class Team_lead(Developer, Manager):
    def __init__(self, team_size, name, salary, programming_language, department):
        self.team_size = team_size
        Developer.__init__(self, name, salary, programming_language)
        Manager.__init__(self, name, salary, department)


def test_check_attributes():
    new = Team_lead(name='Test1', salary=100, team_size=30, programming_language="Python",
                         department='QA Engineer')
    for i in new.__dict__:
        print(i)
    #print(new.__getattribute__("department"), new.__getattribute__("team_size"))



print(test_check_attributes())



