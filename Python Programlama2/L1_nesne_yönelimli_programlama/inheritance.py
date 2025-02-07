class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def show_info(self):
        info = f"""
        Name: {self.name}
        Surname: {self.surname}
        Age: {self.age}
        """
        print(info.strip())


class Teacher(Person):
    def __init__(self, name, surname, age, department):
        super().__init__(name, surname, age)
        self.department = department

    def show_info(self):
        print("Teacher Information")
        super().show_info()
        print(f"Department: {self.department}\n")


class Student(Person):
    def __init__(self, name, surname, age, grade):
        super().__init__(name, surname, age)
        self.grade = grade

    def show_info(self):
        print("Student Information")
        super().show_info()
        print(f"Grade: {self.grade}\n")


# Örnek kullanım
t1 = Teacher("Burak", "Aksoy", 22, "Computer Engineering")
s1 = Student("Ceren", "Alkan", 16, grade=80)

t1.show_info()
s1.show_info()