'''
sınıf : ortak davranış
nesne : sınıf örneği
encapsulation : erişimi sınırlandırma
inheritance : bir sınıftan başka bir sınıf oluşturma. (alt -> üst ilişkisi)
polymorphism : bir metodun bir çok nesne tarafından kullanılması
abstraction : gereksiz karmaşıklık gizlenir.
'''

class Student():   # class structure
    name = ""      #class attributes
    surname = ""
    lesson = []

student1 = Student()    # object is created.
student1.name ="burak"
student1.surname ="aksoy"
student1.lesson.append("türkçe")
student1.lesson.append("mat")

student2 = Student()
student2.name ="ceren"
student2.surname ="alkan"

print(student2.name)
print(student2.surname)
print(student2.lesson)


# self ve init kullanarak

class Students():
    def __init__(self,name,surname,lessons):
        self.name = name
        self.surname = surname
        self.lessons = lessons
        print("name",self.name)
        print("surname",self.surname)
        print("lessons",self.lessons)

s1 = Students("burak","aksoy",["ooad","cnp"])
s2 = Students("ceren","alkan",["highway","yapı statiği","celik"])














