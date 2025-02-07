import sqlite3

database = sqlite3.connect("student1.sqlite")
cursor = database.cursor()  # veritabanı üzerinde işlem yapabilmek için oluşturmamız gerekiyor.

'''
tablo oluşturma , veri tipleri

INTEGER : tam sayılar için
REAL : ondalıklı sayılar için
TEXT : karakter dizileri için
BLOB : binary format için

CREATE TABLO table_name(column1,column2,...)
'''

query = "CREATE TABLE IF NOT EXISTS Student(StudentName TEXT, StudentSurname TEXT, StudentNo INTEGER)"
print(cursor.execute(query))

'''
tabloya kayıt ekleme , veri ekleme
INSERT INTO table_name(column1,column2...) VALUES(value1,value2...)
'''

query2 = "INSERT INTO Student(StudentName,StudentSurname,StudentNo) VALUES('ceren','alkan',41)"
query3 = "INSERT INTO Student(StudentName,StudentSurname,StudentNo) VALUES(?,?,?)"

name = input("your name : ")
surname = input("your surname : ")
no = input("your no : ")

student_info = ("berat", "aksoy", 45)
student_info2 = (name, surname, no)

print(cursor.execute(query2))
print(cursor.execute(query3, student_info2))
database.commit()

'''
kayıt listeleme
SELECT column1,column2,column3.. FROM table_name WHERE query_condition
'''
query4 = "SELECT StudentName,StudentSurname,StudentNo FROM Student"
# query4 = "SELECT StudentName,StudentSurname,StudentNo FROM Student WHERE StudentName = 'burak' "  # koşullu yapı
cursor.execute(query4)
# result = cursor.fetchall()  # tüm kayıtları getirir.
# result = cursor.fetchone()  # tek bir kayıt getirir.
result = cursor.fetchmany(4)  # verilen size kadar kayıt getirir.
print(result)

# for i in cursor:    yukardaki ifadeyi bu şekilde for döngüsüyle de çağırabilirz.
#    print(i)

'''
kayıt güncelleme
UPDATE table_name SET column1 = newValue , column2 = newValue2..WHERE condition .. 
'''

query5 = "UPDATE Student SET StudentName = 'Ceren' ,StudentSurname = 'Alkan' , StudentNo = 3105 WHERE StudentName = 'ceren' "
print(cursor.execute(query5))
database.commit()

'''
kayıt silme
DELETE FROM table_name WHERE delete_condition
'''
query6 = "DELETE FROM Student WHERE StudentName = 'Gökhan'"
print(cursor.execute(query6))
database.commit()
