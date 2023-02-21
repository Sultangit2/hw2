class Human:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Hello, my name is {self.name}.")

class Age:
    def __init__(self, age):
        self.age = age

    def get_older(self):
        self.age += 1
        print(f"I am now {self.age} years old.")

class Student(Human, Age):
    def __init__(self, name, age):
        Human.__init__(self, name)
        Age.__init__(self, age)

    def study(self):
        print(f"{self.name} is studying.")

class Employee:
    def __init__(self, salary):
        self.salary = salary

    def get_raise(self, amount):
        self.salary += amount
        print(f"My salary is now {self.salary}.")

class Graduate(Student, Employee):
    def __init__(self, name, age, degree, salary):
        Student.__init__(self, name, age)
        Employee.__init__(self, salary)
        self.degree = degree

    def graduate(self):
        print(f"{self.name} has graduated with a degree in {self.degree}.")
