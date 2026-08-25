from abc import ABC, abstractmethod


# -------------------------------
# Base Class
# -------------------------------
class Student:
    def __init__(self, name, age, roll_number):
        self.name = name
        self.age = age
        self.roll_number = roll_number

        # Encapsulation
        self.__marks = {}

    def add_marks(self, subject, marks):
        if 0 <= marks <= 100:
            self.__marks[subject] = marks
        else:
            print("Marks should be between 0 and 100.")

    def get_marks(self):
        return self.__marks.copy()


# -------------------------------
# Abstract Class
# -------------------------------
class ReportCard(Student, ABC):

    @abstractmethod
    def generate_report(self):
        pass

    def calculate_total(self):
        marks = self.get_marks()
        return sum(marks.values())

    def calculate_average(self):
        marks = self.get_marks()

        if len(marks) == 0:
            return 0

        return self.calculate_total() / len(marks)

    def calculate_grade(self):
        average = self.calculate_average()

        if average >= 90:
            return "A+"
        elif average >= 80:
            return "A"
        elif average >= 70:
            return "B"
        elif average >= 60:
            return "C"
        elif average >= 50:
            return "D"
        else:
            return "F"

    def check_result(self):
        marks = self.get_marks()

        # Student must score at least 40 in every subject
        for mark in marks.values():
            if mark < 40:
                return "FAIL"

        return "PASS"


# -------------------------------
# Concrete Class
# -------------------------------
class StudentReport(ReportCard):

    # Polymorphism:
    # Implementing the abstract method
    def generate_report(self):

        marks = self.get_marks()
        total = self.calculate_total()
        average = self.calculate_average()
        grade = self.calculate_grade()
        result = self.check_result()

        print("\n========== REPORT CARD ==========")

        print(f"Name       : {self.name}")
        print(f"Age        : {self.age}")
        print(f"Roll Number: {self.roll_number}")

        print("\n---------- Subject Marks ----------")

        for subject, mark in marks.items():
            print(f"{subject:<12}: {mark}")

        print("-----------------------------------")
        print(f"Total      : {total}")
        print(f"Average    : {average:.2f}")
        print(f"Grade      : {grade}")
        print(f"Result     : {result}")

        print("===================================")


# -------------------------------
# Creating Student Object
# -------------------------------

student = StudentReport("Roy", 20, 101)

student.add_marks("Math", 85)
student.add_marks("Python", 92)
student.add_marks("English", 78)
student.add_marks("Science", 88)

student.generate_report()
