import sqlite3

class Student():
    student_list = []

    def __init__(self, name, surname, no, grade):
        self.name = name
        self.surname = surname
        self.no = no
        self.grade = grade

    @classmethod
    def student_add(cls, name, surname, no, grade):
        new_student = Student(name, surname, no, grade)
        cls.student_list.append(new_student)

    @classmethod
    def show_list(cls):
        if not cls.student_list:
            print("No students in the list.")
            return

        for student in cls.student_list:
            print("student name:", student.name)
            print("student surname:", student.surname)
            print("student no:", student.no)
            print("student grade:", student.grade)
            print("****************************")


class DatabaseConnection():
    def __init__(self, database_name, table_name):
        self.database = sqlite3.connect(database_name)
        self.cursor = self.database.cursor()
        self.table = table_name
        query0 = "CREATE TABLE IF NOT EXISTS {} (name TEXT NOT NULL, surname TEXT NOT NULL, no INTEGER PRIMARY KEY AUTOINCREMENT, grade INTEGER NOT NULL)".format(
            self.table)
        self.cursor.execute(query0)
        self.database.commit()

    def student_to_bring(self):
        query = "SELECT * FROM {}".format(self.table)
        self.cursor.execute(query)
        Student.student_list.clear()
        for student in self.cursor:
            Student.student_add(student[0], student[1], student[2], student[3])

    def student_add(self, name, surname, grade):
        try:
            query1 = "INSERT INTO {} (name,surname,grade) VALUES(?,?,?)".format(self.table)
            self.cursor.execute(query1, (name, surname, grade))
            self.database.commit()
            self.student_to_bring()
            print(f"Student {name} {surname} added successfully.")
        except sqlite3.Error as e:
            print(f"Error adding student: {e}")

    def student_delete(self, no):
        try:
            query2 = "DELETE FROM {} WHERE no = ?".format(self.table)
            self.cursor.execute(query2, (no,))
            if self.cursor.rowcount == 0:
                print(f"No student found with number {no}")
            else:
                self.database.commit()
                self.student_to_bring()
                print(f"Student with number {no} deleted successfully.")
        except sqlite3.Error as e:
            print(f"Error deleting student: {e}")

    def student_grade_update(self, grade, no):
        try:
            query3 = "UPDATE {} SET grade = ? WHERE no = ?".format(self.table)
            self.cursor.execute(query3, (grade, no))
            if self.cursor.rowcount == 0:
                print(f"No student found with number {no}")
            else:
                self.database.commit()
                self.student_to_bring()
                print(f"Grade updated successfully for student number {no}")
        except sqlite3.Error as e:
            print(f"Error updating grade: {e}")

    def filter_student_grade(self, minlimit, maxlimit):
        try:
            query4 = "SELECT * FROM {} WHERE grade >= ? AND grade <= ?".format(self.table)
            self.cursor.execute(query4, (minlimit, maxlimit))
            students = self.cursor.fetchall()
            if not students:
                print(f"No students found with grades between {minlimit} and {maxlimit}")
                return

            for student in students:
                print("student name:", student[0])
                print("student surname:", student[1])
                print("student no:", student[2])
                print("student grade:", student[3])
                print("****************************")
        except sqlite3.Error as e:
            print(f"Error filtering students: {e}")

    def close_connect(self):
        try:
            self.database.close()
            print("Database connection closed successfully.")
        except sqlite3.Error as e:
            print(f"Error closing database connection: {e}")

    def __del__(self):
        self.close_connect()


database = DatabaseConnection("StudentGradingSystem_Database.sqlite", "Student")
'''
database.student_add("Ahmet", "Yılmaz", 23)
database.student_add("Zeynep", "Kaya", 45)
database.student_add("Mehmet", "Demir", 78)
database.student_add("Ayşe", "Çelik", 91)
database.student_add("Can", "Özkan", 34)
database.student_add("Elif", "Şahin", 67)
database.student_add("Onur", "Arslan", 89)
database.student_add("Selin", "Aydın", 12)
database.student_add("Emre", "Yıldız", 55)
database.student_add("Deniz", "Öztürk", 43)
'''
# Test kodu
database.student_delete(2)
database.student_grade_update(45, 1)
database.filter_student_grade(45, 85)
database.student_to_bring()
Student.show_list()
