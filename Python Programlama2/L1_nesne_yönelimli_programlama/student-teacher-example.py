class Person():
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def showInfos(self):
        print("name : ", self.name)
        print("surname : ", self.surname)


class Student(Person):
    studentList = []

    def __init__(self, name, surname, studentNo, grade):
        super().__init__(name, surname)
        self.studentNo = studentNo
        self.grade = grade
        self.state = bool()
        self.studentList.append(self)

    def showInfos(self):
        super().showInfos()
        print("student no : ", self.studentNo)
        print("grade : ", self.grade)


class Teacher(Person):
    def __init__(self, name, surname, department):
        super().__init__(name, surname)
        self.department = department

    def showInfos(self):
        super().showInfos()
        print("department : ", self.department)

    def studentState(self):
        total = 0.0
        for student in Student.studentList:
            total += float(student.grade)
        average = total / len(Student.studentList)
        print("average of class : ", average)
        for student in Student.studentList:
            if float(student.grade) >= average:
                print("***********************************")
                student.state = True
                print("Student {} is successful.".format(student.name))

            else:
                print("***********************************")
                student.state = False
                print("Student {} is un-successful.".format(student.name))

    def showStudentInfos(self):
        for student in Student.studentList:
            print("***********************************")
            student.showInfos()
            if student.state == True:
                print("success")
            else:
                print("unsuccess")


t1 = Teacher("muhammed", "erdem", "computer enginnering")
s1 = Student("burak", "aksoy", "6012", "85")
s2 = Student("ceren", "alkan", "3105", "80")
s3 = Student("ali", "bingöl", "5512", "90")
s4 = Student("umut", "uslu", "3141", "60")
s5 = Student("mehmet bakir", "bozkurt", "0001", "10")
t1.showInfos()
t1.studentState()
t1.showStudentInfos()
