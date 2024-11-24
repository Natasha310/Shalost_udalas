# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

class Student:
    def __init__(self, name, surname, age, mid_mark):
        self.name = name
        self.surname = surname
        self.age = age
        self.mid_mark = mid_mark

    def update_mark(self, new_mark):
        self.mid_mark = new_mark
        return new_mark

    def show_student_data(self):
        print(f"Name: {self.name}")
        print(f"Surname: {self.surname}")
        print(f"Age: {self.age}")
        print(f"Middle mark: {self.mid_mark}")

    pass

student1 = Student("Tester", "First", 18, 11)
print("Before update")
student1.show_student_data()
#Updated student mid_mark
student1.update_mark(12)
print("After update")
student1.show_student_data()


